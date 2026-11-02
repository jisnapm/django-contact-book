# Django Contact Book

A simple Contact Book CRUD application built using Python and Django.

## Features

- Add new contacts
- View all contacts
- Retrieve individual contact details
- Update existing contacts
- Delete contacts

## Tech Stack

- Python
- Django
- SQLite
- JSON

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/contacts/add/` | Add a contact |
| GET | `/contacts/` | View all contacts |
| GET | `/contacts/<id>/` | View contact details |
| PUT | `/contacts/update/<id>/` | Update a contact |
| DELETE | `/contacts/delete/<id>/` | Delete a contact |

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/django-contact-book.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-contact-book
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Testing

API endpoints can be tested using Thunder Client or the VS Code REST Client extension.

