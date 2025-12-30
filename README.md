BeyondChats – Phase 1 (Backend Scraping & APIs)
📌 Project Overview

This project is Phase 1 of the BeyondChats Full Stack Developer Intern assignment.

In this phase, I have:

Scraped the 5 oldest blog articles from BeyondChats

Stored them in a database

Created CRUD REST APIs to manage articles

The project is built using Django and Django REST Framework, following clean backend practices.

🛠 Tech Stack

Backend: Django 6.0

API Framework: Django REST Framework

Database: SQLite (can be switched to PostgreSQL)

Scraping: Requests + BeautifulSoup

Language: Python 3.13

Project Structure

beyondchats/
│
├── blogs/
│   ├── models.py       # Article model
│   ├── views.py        # API views
│   ├── serializers.py  # DRF serializers
│   ├── scraper.py      # Blog scraping logic
│   ├── urls.py         # App-level routes
│
├── beyondchats/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── README.md


🧩 Phase 1 Features Implemented
✅ Blog Scraping

Scrapes 5 oldest articles from
👉 https://beyondchats.com/blogs/

Extracts:

Title

Source URL

Saves data into database

✅ Database Storage

Articles stored using Django ORM

Prevents duplicate entries

✅ REST APIs (CRUD)

| Method | Endpoint              | Description        |
| ------ | --------------------- | ------------------ |
| GET    | `/api/articles/`      | List all articles  |
| POST   | `/api/articles/`      | Create new article |
| GET    | `/api/articles/<id>/` | Get single article |
| PUT    | `/api/articles/<id>/` | Update article     |
| DELETE | `/api/articles/<id>/` | Delete article     |


⚙️ Local Setup Instructions

# Clone repository
git clone <your-repo-url>
cd beyondchats

# Create virtual environment
python -m venv bchat
bchat\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver

🌐 API URLs (Working)

✅ http://127.0.0.1:8000/api/articles/

✅ http://127.0.0.1:8000/api/articles/1/

❌ http://127.0.0.1:8000/

(Expected behavior – no homepage configured)

Data Flow / Architecture Diagram

BeyondChats Website
        ↓
Python Scraper (BeautifulSoup)
        ↓
Django Models (Article)
        ↓
SQLite Database
        ↓
Django REST APIs
        ↓
API Consumers (Postman / Frontend)







