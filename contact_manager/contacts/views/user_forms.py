from django.shortcuts import render, redirect
from contacts.forms import RegisterForm
from django.contrib import messages


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
