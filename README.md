Contact Manager
===============

A simple yet full-featured **Django-based contact management application**.  
It allows authenticated users to create, view, update, delete, and search contacts, with support for categories and optional profile pictures. Includes a **landing page**, production-ready static files (WhiteNoise), and optional deployment on **Render** with PostgreSQL.

> **Portfolio project** — This is **not a commercial product**. It is a **demonstration project** for portfolio purposes, showcasing Django skills and practices.

### Features

- **Landing page** – Home at `/` with hero section and feature highlights
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
  - Optional image upload for each contact (Pillow)
- **Seed data** – Management command to populate the database with fake contacts (Faker)

---

## Tech Stack

- **Language**: Python
- **Framework**: Django
- **Database**: SQLite (local) / PostgreSQL (production, e.g. Render)
- **Templates**: Django Template Language (DTL), global base in `base_templates/`
- **Static files**: WhiteNoise (production), global CSS in `base_static/`
- **Production server**: Gunicorn
- **Other**: dj-database-url, Pillow (images), Faker (seed data)

---

## Project Structure (Relevant Parts)

- `manage.py` – Django management script
- `contact_manager/` – Django project configuration (settings, URLs, WSGI/ASGI)
  - `settings.py` – Base config; production uses env vars and `dj_database_url`
  - `local_settings.py` – Local overrides (SECRET_KEY, DEBUG, ALLOWED_HOSTS); not committed
- `base_templates/` – Global templates
  - `global/base.html` – Base layout
  - `global/partials/` – _head, _header, _footer, _messages, _pagination
- `base_static/` – Global static files (e.g. `global/css/styles.css`)
- `contacts/` – Main application
  - `models.py` – `Category` and `Contact` models
  - `views/` – Views for home, listing, searching, CRUD, and user actions
  - `urls.py` – App URL routes
  - `templates/contacts/` – HTML templates (home, index, contact, forms, etc.)
  - `management/commands/seed.py` – `python manage.py seed` to populate fake contacts
- `utils/create_contacts_faker.py` – Standalone script to generate many fake contacts (optional)
- `requirements.txt` – Python dependencies (Django, WhiteNoise, Gunicorn, Pillow, Faker, etc.)

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

```bash
pip install -r requirements.txt
```

This installs Django, WhiteNoise, Gunicorn, Pillow, Faker, dj-database-url, psycopg2-binary, and other dependencies (see `requirements.txt`).

### 4. Configure environment (local development)

For local development, the project uses `contact_manager/local_settings.py` (not in version control) to override:

- `SECRET_KEY`
- `DEBUG = True`
- `ALLOWED_HOSTS = []`

Create `contact_manager/local_settings.py` with your local values, or the app may fall back to base settings (which expect env vars and are aimed at production).

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

The application will be available at `http://127.0.0.1:8000/`. You’ll see the **landing page** first; use “View Contacts” or go to `/contacts/` for the contact list.

### 8. (Optional) Seed the database with fake contacts

```bash
python manage.py seed
```

This creates categories (Friends, Family, Work) and 40 fake contacts using Faker (pt_BR). It skips if contacts already exist.

---

## Usage

1. Open `http://127.0.0.1:8000/` in your browser (landing page).
2. Use **View Contacts** or go to `/contacts/` for the contact list.
3. Register a new user or log in with an existing account.
4. Create new contacts via the **Create Contact** page.
5. Use the search bar to find contacts by name, phone, or email.
6. Click on a contact to view its detailed page.
7. Edit or delete contacts as needed.

---

## URL Overview

Routes defined by the `contacts` app (namespace `contacts:`):

| Path | Name | Description |
|------|------|-------------|
| `/` | `home` | Landing page |
| `/contacts/` | `index` | Contact list (paginated) |
| `/search/` | `search` | Contact search |
| `/contact/<id>/` | `contact` | Contact detail |
| `/contact/create/` | `create` | Create new contact |
| `/contact/<id>/update/` | `update` | Update contact |
| `/contact/<id>/delete/` | `delete` | Delete contact |
| `/user/create/` | `register` | User registration |
| `/user/login/` | `login` | User login |
| `/user/logout/` | `logout` | User logout |
| `/user/update/` | `user_update` | User profile update |

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

The project is set up for deployment on **Render** (or similar):

- **Base settings** use environment variables: `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` (e.g. `.onrender.com`).
- **Database**: `dj-database-url` reads `DATABASE_URL` (PostgreSQL on Render); locally defaults to SQLite.
- **Static files**: WhiteNoise serves static files; `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'`.
- **WSGI**: Use Gunicorn as the process command, e.g. `gunicorn contact_manager.wsgi:application`.
- Set `DEBUG = False` in production and configure `ALLOWED_HOSTS` for your domain.
- Serve media uploads via a persistent volume or external storage if required.

---

## License

This project is **not a product** — it is a **portfolio demonstration** for learning and showcasing skills.  
Provided as-is; you can adapt it to your needs. If you plan to publish derivatives, consider adding an explicit license (e.g., MIT, BSD).

---

## Project Links

- **Repository**: `https://github.com/SilvanoMarini/ContactManager`
- **Author GitHub**: `https://github.com/SilvanoMarini`
- **LinkedIn**: `https://www.linkedin.com/in/silvanomarini`

## Contact

If you have questions, suggestions, or feedback, feel free to reach out:

- **Email**: `silvano.marini.dev@gmail.com`
