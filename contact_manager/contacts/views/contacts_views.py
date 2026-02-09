from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
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


def search(request):
    searched_contact = request.GET.get('q', '').strip()


# Redirect to index if search query is empty
# to avoid unnecessary database querie
    if searched_contact == '':
        return redirect('contacts:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(Q(first_name__icontains=searched_contact) |
                Q(last_name__icontains=searched_contact) |
                Q(phone__icontains=searched_contact) |
                Q(email__icontains=searched_contact)
                )\
        .order_by('first_name', 'last_name')

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contacts/index.html',
        context=context
    )
