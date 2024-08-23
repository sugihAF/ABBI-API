# ABBI-API

ABBI-API (Ayo Belajar Bahasa Isyarat) is a Django-based API developed to support Machine Learning (ML) hand recognition for Indonesian Sign Language, covering both SIBI (Sistem Isyarat Bahasa Indonesia) and BISINDO (Bahasa Isyarat Indonesia). This API provides tools and resources for recognizing and processing sign language gestures, making it easier to develop applications that support the deaf community in Indonesia.

## Features

- **Django Backend:** Robust data management and API endpoints using Django ORM.
- **Hand Recognition API:** Supports ML models for recognizing SIBI & BISINDO gestures.
- **SQLite Database:** Easy-to-use database for development and testing.
- **Web Interface:** Basic templates and static files included for web-based management.
- **Heroku Deployment:** Pre-configured for deployment on Heroku.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Python 3.8+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sugihAF/ABBI-API.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ABBI-API
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

### Running the Application

Start the Django development server:

```bash
python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/.

###Deployment
For deployment on Heroku:

1. Ensure heroku-cli is installed and logged in.
2. Create a new Heroku app and push the repository.
3. Set up the environment variables as per runtime.txt and Procfile.
