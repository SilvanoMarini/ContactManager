from django.shortcuts import render, redirect
from contacts.forms import ContactForm


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'site_title': ' Create Contact | ',
            'form': form,
        }

        if form.is_valid():
            form.save()
            return redirect('contacts:create')

        return render(
            request,
            'contacts/create.html',
            context=context
        )

    context = {
        'site_title': ' Create Contact | ',
        'form': ContactForm(),
    }

    return render(
        request,
        'contacts/create.html',
        context=context
    )
