from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    # new_field = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('url', 'location', 'company')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'sex', 'home_university', 'faculty', 'motivation', 'social_network_account']

class NARFUForm(forms.ModelForm):
    # TRUE_FALSE_CHOICES = (
    #     (True, 'Male'),
    #     (False, 'Female')
    # )
    # sex = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Sex",
    #                               initial='', widget=forms.Select(), required=True)
    # # sex = forms.BooleanField(widget='Select')
    # home_university = forms.CharField(max_length=150)
    # faculty = forms.CharField(max_length=150)
    # motivation = forms.CharField(max_length=1500)
    # social_network_account = forms.CharField(max_length=150)
    class Meta:
        model = Profile
        fields = ['sex', 'home_university', 'faculty', 'motivation', 'social_network_account']