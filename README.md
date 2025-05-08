# PDF Generator

This is a small Python script that generates PDF files from HTML templates. It's a simple proof-of-concept project, but it gets the job done if you're looking to automate basic PDF creation.

## Requirements

Make sure you have the following installed:

- Python 3.7+
- `wkhtmltopdf` – You can install it from https://wkhtmltopdf.org/downloads.html

## Installation

```bash
git clone <this-repo-url>
cd pdfgenerator
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

Make sure `wkhtmltopdf` is installed and added to your system's PATH. You can test it by running:

```bash
wkhtmltopdf --version
```

## Usage

Edit the `sample_template.html` to your needs, then run:

```bash
python pdfgen.py
```

It will create a `sample_output.pdf` in the current directory.

## Notes

This is just a quick utility script. Feel free to expand it with CLI arguments, better templating support, or integration into a bigger app.
