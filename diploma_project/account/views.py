from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators   import login_required

from .forms import CreateUserForm

@login_required(login_url='log_page')
def personal_page(request):
    return render(request, 'personal_page.html', {})

def reg_page(request):
    if request.user.is_authenticated:
        return redirect('personal_page')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Account was created by' + user)
               return redirect('log_page')

        return render(request, 'register.html', {'form': form} )


def log_page(request):
    if request.user.is_authenticated:
        return redirect('personal_page')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('personal_page')
            else:
                messages.info(request, 'User or Password was not given')
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('log_page')


class PasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'password_reset.html'

def password_success(request):
    return render(request, 'password_send.html')

class PasswordSetView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'reset_form.html'

def changed_password_message(request):
    return render(request, 'changed_password_message.html')
    
# Create your views here.
