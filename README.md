Contact Manager
===============

A simple yet full-featured **Django-based contact management application**.  
It allows authenticated users to create, view, update, delete, and search contacts, with support for categories and optional profile pictures.

### Features

- **Contact CRUD**
  - Create, read, update, and delete contacts
  - Fields include first name, last name, phone, email, description, picture, and creation date
- **Categories**
  - Group contacts using customizable categories
- **Search & Pagination**
  - Search contacts by first name, last name, phone, or email
  - Paginated contact list for better navigation
- **Authentication**
  - User registration, login, logout, and profile update
  - Each contact can be associated with an owner (`User`)
- **Visibility Control**
  - Flag to show/hide contacts from the main list
- **Profile Pictures**
  - Optional image upload for each contact

---

## Tech Stack

- **Language**: Python
- **Framework**: Django
- **Database**: SQLite (default Django configuration; can be changed)
- **Templates**: Django Template Language (DTL)

---

## Project Structure (Relevant Parts)

- `manage.py` – Django management script
- `contact_manager/` – Django project configuration (settings, URLs, WSGI/ASGI)
- `contacts/` – Main application
  - `models.py` – `Category` and `Contact` models
  - `views/` – Views for listing, searching, CRUD, and user actions
  - `urls.py` – App URL routes
  - `templates/contacts/` – HTML templates (list, detail, forms, etc.)

---

## Getting Started

### Prerequisites

- **Python 3.10+** (recommended)
- **pip** (Python package manager)
- **virtualenv** (optional but recommended)

### 1. Clone the repository

```bash
git clone https://github.com/SilvanoMarini/ContactManager.git
cd ContactManager
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

### 3. Install dependencies

If you already have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install at least:

```bash
pip install django
```

### 4. Configure environment variables (optional but recommended)

In production or advanced setups, you should configure:

- `DJANGO_SECRET_KEY`
- `DEBUG` (set to `False` in production)
- `ALLOWED_HOSTS`

You can store these in a `.env` file and load them in your settings if desired.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

Follow the interactive prompts to set username, email, and password.

### 7. Run the development server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

---

## Usage

1. Open `http://127.0.0.1:8000/` in your browser.
2. Register a new user or log in with an existing account.
3. Create new contacts via the **Create Contact** page.
4. Use the search bar to find contacts by name, phone, or email.
5. Click on a contact to view its detailed page.
6. Edit or delete contacts as needed.

---

## URL Overview

These are the main routes defined by the `contacts` app:

- `/` – Contact list (index)
- `/search/` – Contact search
- `/contact/<id>/` – Contact detail
- `/contact/create/` – Create new contact
- `/contact/<id>/update/` – Update existing contact
- `/contact/<id>/delete/` – Delete contact
- `/user/create/` – User registration
- `/user/login/` – User login
- `/user/logout/` – User logout
- `/user/update/` – User profile update

Note: Routes may be namespaced under `contacts:` in Django templates and redirects.

---

## Models Overview

- **Category**
  - `name` – Unique name of the category

- **Contact**
  - `first_name`, `last_name`
  - `phone`, `email`
  - `description`
  - `created_date`
  - `show` (boolean to control visibility)
  - `picture` (optional image upload)
  - `category` (optional foreign key to `Category`)
  - `owner` (optional foreign key to `User`)

---

## Running Tests

If you have tests defined for the `contacts` app, you can run them with:

```bash
python manage.py test
```

---

## Deployment Notes

- Set `DEBUG = False` in production.
- Configure `ALLOWED_HOSTS` properly.
- Use a production-ready database (e.g., PostgreSQL) instead of SQLite.
- Serve static and media files via a proper web server (Nginx, Apache, etc.).
- Use a WSGI/ASGI server like Gunicorn or uWSGI for production.

---

## License

This project is provided as-is for learning and personal use.  
You can adapt it to your needs; if you plan to publish it, consider adding an explicit license (e.g., MIT, BSD, etc.).

---

## Project Links

- **Repository**: `https://github.com/SilvanoMarini/ContactManager`
- **Author GitHub**: `https://github.com/SilvanoMarini`

## Contact

If you have questions, suggestions, or feedback, feel free to reach out:

- **Email**: `silvano.marini.dev@gmail.com`
