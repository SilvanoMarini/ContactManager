from django import forms
from contacts.models import Contact
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone',
                  'email', 'description', 'category',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        return super().clean()

    def clean_first_name(self):
        cleaned_data = self.cleaned_data['first_name']
        errors = []

        if len(cleaned_data) < 2:
            errors.append(ValidationError(
                "First name must be at least 2 characters long.",
                code='too_short',
            ))

        if cleaned_data.isnumeric():
            errors.append(ValidationError(
                "First name must not be numeric.",
                code='is_numeric',
            ))

        if errors:
            raise ValidationError(errors)

        return cleaned_data

    def clean_last_name(self):
        cleaned_data = self.cleaned_data['last_name']
        errors = []

        if len(cleaned_data) < 2:
            errors.append(ValidationError(
                "last name must be at least 2 characters long.",
                code='too_short',
            ))

        if cleaned_data.isnumeric():
            errors.append(ValidationError(
                "Last name must not be numeric.",
                code='is_numeric',
            ))

        if errors:
            raise ValidationError(errors)

        return cleaned_data
