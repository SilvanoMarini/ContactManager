from django.shortcuts import render
from contacts.models import Contact

context = {
    'contacts': Contact.objects.all()
}

def index(request):
    return render(
    request,
    'contacts/index.html',
    context=context
    )