from django.shortcuts import render, get_object_or_404
from contacts.models import Contact


def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('first_name', 'last_name')

    context = {
        'contacts': contacts,
        'site_title': 'Contacts | '
    }

    return render(
        request,
        'contacts/index.html',
        context=context
    )


def contact(request, contact_id):
    sigle_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'contact': sigle_contact,
        'site_title': f'{sigle_contact} | '
    }

    return render(
        request,
        'contacts/contact.html',
        context=context
    )
