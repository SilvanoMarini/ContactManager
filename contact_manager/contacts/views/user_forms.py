from django.shortcuts import render, redirect
from contacts.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully registered.')
            return redirect('contacts:index')

    return render(
        request,
        'contacts/register.html',
        context={
            'site_title': 'Register User | ',
            'form': form,

        }
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            print(user)
            messages.success(request, 'User successfully logged in.')
            return redirect('contacts:index')

        messages.error(request, 'Invalid username or password.')

    return render(
        request,
        'contacts/login.html',
        context={
            'site_title': 'Login User | ',
            'form': form,
        }
    )


def logout_view(request):
    auth.logout(request)
    messages.success(request, 'User successfully logged out.')
    return redirect('contacts:login')
