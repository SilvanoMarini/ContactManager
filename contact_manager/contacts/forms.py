from django import forms
from contacts.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


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


class RegisterUpdateForm(forms.ModelForm):
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

    password1 = forms.CharField(
        required=False,
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='Enter the same password as before, for verification.',
        required=False
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)
        if commit:
            user.save()

        return user

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', 'Passwords do not match.')

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if email != current_email:
            if User.objects.filter(email=email).exists():
                raise ValidationError('Email already exists.')
            return email

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as error:
                self.add_error('password1', error)

        return password1
