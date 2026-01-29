Grocery Store Web Application (Django)

A Django-based grocery store web application that allows users to browse products by category, add items to a cart, update quantities dynamically, and place orders.
This project demonstrates full-stack web development using Django, MySQL, HTML, CSS, Bootstrap, and session-based cart management.

## Features:
Home page with product categories.

Category-wise product listing

Search products by name

Add to cart without page refresh

Cart page with total price calculation

Checkout flow (payment page placeholder)

Admin panel to manage:
Categories
Products (with images)
Orders

Session-based cart (no login required)

## Tech Stack

Backend: Python, Django
Frontend: HTML, CSS, Bootstrap
Database: MySQL (can also work with SQLite)


##  How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/saikiran20018/grocery-store-django.git
cd grocery-store-django

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install django mysqlclient

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Run server
python manage.py runserver

## Author:

Saikiran Thippirishetty

GitHub: https://github.com/saikiran20018

LinkedIn: linkedin.com/in/saikiranthippirishetty
