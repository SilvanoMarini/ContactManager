from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contacts.forms import ContactForm
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def create(request):
    form_action = reverse('contacts:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            'site_title': ' Create Contact | ',
            'form': form,


        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contact successfully created.')
            return redirect('contacts:update', contact_id=contact.pk)

        return render(
            request,
            'contacts/create.html',
            context=context
        )

    context = {
        'site_title': ' Create Contact | ',
        'form': ContactForm(),
        'form_action': form_action,
        'send': 'create',
    }

    return render(
        request,
        'contacts/create.html',
        context=context
    )


@login_required
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    form_action = reverse('contacts:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'site_title': ' Update Contact | ',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contact successfully updated.')
            return redirect('contacts:update', contact_id=contact.pk)

        return render(
            request,
            'contacts/create.html',
            context=context
        )

    context = {
        'site_title': ' Update Contact | ',
        'form': ContactForm(instance=contact),
        'form_action': form_action,
        'send': 'update',
    }

    return render(
        request,
        'contacts/create.html',
        context=context
    )


@login_required
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    confirmation = request.POST.get('confirmation', 'no')
    print('confirmation', confirmation)

    if confirmation == 'yes':
        contact.delete()
        messages.success(request, 'Contact successfully deleted.')
        return redirect('contacts:index')

    return render(
        request,
        'contacts/contact.html',
        context={
            'contact': contact,
            'confirmation': confirmation
        }
    )
