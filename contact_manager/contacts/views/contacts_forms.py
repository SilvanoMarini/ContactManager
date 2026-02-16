from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contacts.models import Contact


def create(request):
    context = {
        'site_title': ' Create Contact | '
    }

    return render(
        request,
        'contacts/create.html',
        context=context
    )
