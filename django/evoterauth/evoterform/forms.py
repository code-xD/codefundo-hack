from django import forms


class EVoterForm(forms.Form):
    voter_name = forms.CharField(max_length=200, label='Name(as per Aadhar Card)')
    age = forms.IntegerField()
    gender = forms.IntegerField()
    aadhar_no = forms.IntegerField(label="Aadhar Card Number")
    aLine1 = forms.CharField(label="Address Line 1", max_length=500)
    aLine2 = forms.CharField(label="Address Line 2", max_length=500)
    s_code = forms.Field(label="State")
    c_code = forms.IntegerField(label="City")
    d_code = forms.IntegerField(label="Town/Village")
    pin = forms.IntegerField(label="Pincode")
