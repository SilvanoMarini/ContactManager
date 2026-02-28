from django.shortcuts import render, redirect
from contacts.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully registered.')
            return redirect('contacts:login')

    return render(
        request,
        'contacts/register.html',
        context={
            'site_title': 'Register User | ',
            'form': form,
            'send': 'Register',

        }
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'User successfully logged in.')

            next_url = request.GET.get('next')
            return redirect(next_url if next_url else 'contacts:index')
        messages.error(request, 'Invalid username or password.')

    return render(
        request,
        'contacts/login.html',
        context={
            'site_title': 'Login User | ',
            'form': form,
            'send': 'Login',
        }
    )


@login_required
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'User successfully logged out.')
    return redirect('contacts:login')


@login_required
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()

            if form.cleaned_data.get('password1'):
                update_session_auth_hash(request, user)

            messages.success(request, 'User successfully updated.')
            return redirect('contacts:user_update')

        messages.error(request, 'Invalid data')

    return render(
        request,
        'contacts/user_update.html',
        context={
            'site_title': 'Update User | ',
            'form': form,
            'send': 'Update',
        }
    )
