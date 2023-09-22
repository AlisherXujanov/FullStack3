import logging
from math import e

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, UserForm, UserUpdateForm
from .usecases import *

log = logging.getLogger(__name__)


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/create_user.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/create_user.html', context)


@login_required
def profile(request):

    if request.method == 'POST':
        p_form = ProfileForm(request.POST,
                             instance=request.user.profile,
                             files=request.FILES)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=True)
            profile = p_form.save(commit=True)
            messages.success(request,
                             f"Your account has been updated!")
            return redirect('profile')
        else:
            context = {
                "u_form": u_form,
                "p_form": p_form,
            }
            return render(request, 'profile.html', context)

    context = {
        'u_form': UserUpdateForm(instance=request.user),
        'p_form': ProfileForm(instance=request.user.profile)
    }
    return render(request, 'profile.html', context)
