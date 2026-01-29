from django.shortcuts import render
from contacts.models import Contact

def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('first_name', 'last_name')

    context = {
        'contacts': contacts
    }

    return render(
        request,
        'contacts/index.html',
        context=context
    )