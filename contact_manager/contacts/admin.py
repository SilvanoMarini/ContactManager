from django.contrib import admin
from contacts import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model.
    Defines list display, filtering, search behavior,
    ordering, and pagination for the Django Admin interface.
    """
    list_display = (
        'id', 'first_name', 'last_name', 'phone', 'email', 'created_date'
    )
    ordering = (
        '-id',
    )
    list_filter = (
        'created_date',
    )
    search_fields = (
        'first_name', 'last_name', 'phone', 'email'
    )
    list_display_links = (
        'id', 'first_name',
    )
    list_per_page = 10
    list_max_show_all = 100
