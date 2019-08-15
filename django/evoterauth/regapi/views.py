from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from evoterform.functions import genrandomstring
from .models import API, Event, Login_Token, Allowed_user, Event_token
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
import json
import requests
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from evoterform.models import AccountDetail
from userauth.encryption import genspkey, decrypt, gen2key
from userauth.models import OTP


@csrf_exempt
def CreateTokenView(request):
    try:
        if request.method == 'POST':
            request_dict = json.loads(request.body)
            api_key = request_dict['api_key']
            api_secret = request_dict['api_secret']
            event_id = request_dict['event_id']
            api = API.objects.get(api_key=api_key, api_secret=api_secret)
            print(api)
            event = Event.objects.get(api=api, event_id=event_id)
            token = genrandomstring(32)
            login_token = Login_Token(token=token, event=event)
            login_token.save()
            return JsonResponse({'login_token': login_token.token})
    except Exception:
        return HttpResponseNotFound()
    return HttpResponseNotFound()


def APIVoterLogin(request, token):
    logout(request)
    username = password = ''
    try:
        login_token = Login_Token.objects.get(token=token, expiry_date__gte=timezone.now())
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            filter_api = login_token.event.api
            users = Allowed_user.objects.all().filter(api=filter_api)
            user_list = []
            for usr in users:
                user_list.append(usr.user)
            if user is not None:
                if user not in user_list:
                    return HttpResponse('You are not registered for this corporation.')
                if len(Event_token.objects.filter(event=login_token.event, user=user)) != 0:
                    return HttpResponse('You have already voted.')
                if user.is_active:
                    data = AccountDetail.objects.get(voterID=user.username)
                    keys = gen2key()
                    otps = OTP.objects.all().filter(account=user)
                    for otp in otps:
                        otp.delete()
                    otp = OTP(message=keys[2], encrypt=keys[1], private_key=keys[0], account=user)
                    mailbody = f"""
                    Dear User,
                    You are mailed a text enter it in appropriate field-
                    Line 1 : '{keys[0]}'
                    Line 1 : '{keys[1]}'
                    Regards,
                    MainAdmin
                    (EVoterAuth)
                    """
                    send_mail('OTP has been mailed', mailbody, 'admin@evoter.com', [data.email])
                    otp.save()
                    return redirect(reverse('otp-api-view', args=(user.username, login_token.token,)))
        return render(request, 'regapi/mainlogin.html')
    except Exception:
        return HttpResponseNotFound()


def APIVoterOTP(request, user, token):
    try:
        user = User.objects.get(username=user)
        otp = OTP.objects.get(account=user, expiry_date__gte=timezone.now())
        login_token = Login_Token.objects.get(token=token, expiry_date__gte=timezone.now())
        if request.POST:
            line1 = request.POST['Line 1']
            line2 = request.POST['Line 2']
            if decrypt(line1, line2, otp.message):
                otp.delete()
                key = login_token.event.private_key
                key_list = genspkey(key)
                event_token = Event_token(event=login_token.event,
                                          user=User.objects.get(username=user), token=key_list[0])
                event_token.save()
                user_data = {
                    'Event_ID': event_token.event.event_id,
                    'user_token': key_list[1]
                }
                requests.post(event_token.event.api.callback_url, json=user_data)
                return redirect(event_token.event.api.redirect_url)
            else:
                messages.error(request, 'The OTP did not match.')
        return render(request, 'regapi/otplogin.html')
    except Exception:
        otps = OTP.objects.all().filter(account=user)
        for opt in otps:
            opt.delete()
        return HttpResponseNotFound()


@csrf_exempt
def VerifyTokenView(request):
    try:
        if request.method == 'GET':
            request_dict = json.loads(request.body)
            api_key = request_dict['api_key']
            api_secret = request_dict['api_secret']
            event_id = request_dict['event_id']
            usertoken = request_dict['user_token']
            api = API.objects.get(api_key=api_key, api_secret=api_secret)
            event = Event.objects.get(api=api, event_id=event_id)
            events = Event_token.objects.all().filter(event=event).values_list('token', flat=True)
            for i in range(len(events)):
                if decrypt(event.private_key, usertoken, events[i]):
                    return JsonResponse({'verified': True})
            return JsonResponse({'verified': False})
    except Exception:
        return HttpResponseNotFound()
