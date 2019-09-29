from django import forms
from django.contrib.auth.models import User
from basic_App.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=500,required=False)

    class Meta:
        model =  User
        fields = ('username','email','password')



class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

