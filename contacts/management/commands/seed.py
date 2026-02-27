from django.core.management.base import BaseCommand
from faker import Faker
from random import choice
from datetime import datetime
from contacts.models import Category, Contact


class Command(BaseCommand):
    help = "Popula o banco com dados fake"

    def handle(self, *args, **kwargs):

        NUMBER_OF_OBJECTS = 40  # Use 40 para portfólio (1000 é exagero)

        if Contact.objects.exists():
            self.stdout.write(self.style.WARNING("Banco já populado."))
            return

        fake = Faker('pt_BR')

        categories_names = ['Friends', 'Family', 'Work']
        django_categories = []

        for name in categories_names:
            category, _ = Category.objects.get_or_create(name=name)
            django_categories.append(category)

        django_contacts = []

        for _ in range(NUMBER_OF_OBJECTS):
            profile = fake.profile()
            email = profile['mail']
            first_name, last_name = profile['name'].split(' ', 1)
            phone = fake.phone_number()
            created_date: datetime = fake.date_this_year()
            description = fake.text(max_nb_chars=100)
            category = choice(django_categories)

            django_contacts.append(
                Contact(
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    email=email,
                    created_date=created_date,
                    description=description,
                    category=category,
                )
            )

        Contact.objects.bulk_create(django_contacts)

        self.stdout.write(self.style.SUCCESS(
            f"{NUMBER_OF_OBJECTS} contatos criados com sucesso!"))
