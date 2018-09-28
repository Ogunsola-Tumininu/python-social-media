from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in user
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
        return render(request, 'accounts/reg_form.html', {'form': form})

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = { "user": user }
    return render(request, 'accounts/profile.html', args) 

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form': form}) 

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        messages.success(request, 'Your password was succefully updated')
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else: 
            messages.error(request, 'Please correct the error below')
            return redirect('change_password')
        
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/change-password.html', {'form': form}) 