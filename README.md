# Django PDF Generator Web App

This is a Django web application that generates PDF files from HTML templates. It provides a user-friendly interface for creating and managing PDF documents with saved templates.

## Features

- Web-based interface for PDF generation
- Template management system
- Saved PDF history
- User authentication (optional)
- Responsive design

Make sure you have the following installed:

- Python 3.7+
- Django 3.0+
- `wkhtmltopdf` – You can install it from https://wkhtmltopdf.org/downloads.html

## Installation

```bash
git clone <this-repo-url>
cd pdfgenerator
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
wkhtmltopdf --version
python manage.py migrate
python manage.py createsuperuser
```

Make sure `wkhtmltopdf` is installed and added to your system's PATH. You can test it by running:

```bash
wkhtmltopdf --version
```

## Usage

1. Template Management:
    - Create and edit HTML templates in the admin interface
    - Use Django template tags for dynamic content

2. PDF Generation:
    - Select a template from your saved templates
    - Fill in any required variables
    - Generate and download the PDF

3. History:
    - View previously generated PDFs
    - Re-generate or download past PDFs

## Project Structure

```
pdfgenerator/
├── pdfgenerator/
├── pdf/                # Main PDF generation app
│   ├── models.py       # Template and PDF history models
│   ├── views.py        # PDF generation views
│   └── templates/      # HTML templates
├── db.sqlite3/             # Database file
└── manage.py               # Django management script
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
