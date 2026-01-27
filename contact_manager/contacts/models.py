from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """
    Represents a contact stored in the agenda, containing personal
    and communication information such as name, phone number,
    email, description, and creation date.
    """

    first_name = models.CharField(
        max_length=50,
        help_text="First name of the contact"
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        help_text="Last name of the contact (optional)"
    )
    phone = models.CharField(
        max_length=20,
        help_text="Primary phone number of the contact"
    )
    email = models.EmailField(
        max_length=254,
        blank=True,
        help_text="Email address of the contact (optional)"
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        help_text="Date and time when the contact was created"
    )
    description = models.TextField(
        blank=True,
        help_text="Additional notes or description about the contact (optional)"
    )

    def __str__(self):
        """
        Returns a string representation of the contact, consisting of
        first name and last name separated by a space, and stripped
        of any trailing whitespace.
        """
        return f"{self.first_name} {self.last_name}".strip()