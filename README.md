# Expense Tracker - Python Capstone Project | Codomax Internship

## 1. System Architecture
- Frontend: HTML (in templates folder)
- Backend: Python Flask
- Database: SQLite
- Logging: Python logging module for error tracking
- Deployment: Render / Gunicorn

## 2. Database Schema
Table: expenses
- id (INTEGER PRIMARY KEY)
- title (TEXT) - Expense title
- amount (REAL) - Expense amount  
- category (TEXT) - Food, Travel, etc
- date (TEXT) - Auto generated date

## 3. Setup Instructions
pip install -r requirements.txt
python app.py
Open: http://127.0.0.1:5000

## 4. Features
- Add Expense with category
- Delete Expense
- Total Spent Calculation
- Exception Safety (try-except)
- Logging (app.log)

## 5. Live Demo
[Render link yaha ayega]

Developed by: Ayush Kumar
Internship: Codomax Digital Solutions - Module 06 Capstone
