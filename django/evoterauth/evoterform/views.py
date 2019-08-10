from django.shortcuts import render, redirect
from .forms import EVoterForm
from .blockchain import runblockchain
import requests
# Create your views here.


def EVoterFormView(request):
    if request.method == 'POST':
        form = EVoterForm(request.POST)
        if form.is_valid():
            voterdata = form.cleaned_data
            if not voterdata['age'] < 18:
                templatedata = requests.get(
                    f"http://dataset-codefundo.herokuapp.com/details/{voterdata['aadhar_no']}", auth=('testuser', 'codefundo'))
                status = runblockchain(voterdata, templatedata.json())
                print(status)
                return redirect('/')
    form = EVoterForm()
    return render(request, 'evoterform/mainform.html', {'form': form})
