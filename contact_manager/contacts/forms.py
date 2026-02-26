from django import forms
from contacts.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        ),
        help_text=(
            'Profile picture of the contact (optional)'
        )
    )

    class Meta:
        model = Contact
        fields = [
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        ]

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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        min_length=2,
        required=True,
        help_text=(
            'First name of the user'
        ),
    )

    last_name = forms.CharField(
        max_length=50,
        min_length=2,
        required=True,
        help_text=(
            'Last name of the user'
        ),
    )

    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text=(
            'Email address of the user'
        ),
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists.')
        return email
