from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, NARFUForm
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        pr_form = NARFUForm(request.POST)
        if user_form.is_valid() and pr_form.is_valid():
            user_form.save()
            user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password1'])
            pr_form = NARFUForm(request.POST, instance=user.profile)
            pr_form.save()
            r_email = user_form.cleaned_data['email']
            name = user_form.cleaned_data['username']
            firstname = user_form.cleaned_data['first_name']
            lastname = user_form.cleaned_data['last_name']
            sex = pr_form.cleaned_data['sex']
            home_university = pr_form.cleaned_data['home_university']
            faculty = pr_form.cleaned_data['faculty']
            motivation = pr_form.cleaned_data['motivation']
            social_network_account = pr_form.cleaned_data['social_network_account']
            email_from = settings.EMAIL_HOST_USER
            if sex == True:
                sex = 'Female'
            else:
                sex = 'Male'
            subjectNARFU = f'New user: {name}.  '
            messageNARFU = f"Name - {firstname}#" \
                           f"Last Name - {lastname}#" \
                           f"E-mail - {r_email}#" \
                           f"University - {home_university}#" \
                           f"Sex - {sex}#" \
                           f"Faculty - {faculty}#" \
                           f"Motivation - {motivation}#" \
                           f"Social Account - {social_network_account}  "

            r_subject = f"Welcome to IT-School"
            r_message = f"Hello,  {name}, you have been successfully registered in IT-School!"
            recip = 'itschoolfeedback@gmail.com'
            recipient_list = [recip, ]
            r_recip = r_email
            r_recipient_list = [r_email, ]
            # send_mail(r_subject, r_message, email_from, r_recipient_list)
            messages.success(request, f'You have been registered. Now you can login to your account')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        pr_form = NARFUForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'pr_form': pr_form })


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'users/profile.html', context)


def update(request):
    if request.method == 'POST':
        pr_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if pr_form.is_valid():
            pr_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('register')
    else:
        pr_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'pr_form': pr_form
    }
    return render(request, 'users/register.html', context)
