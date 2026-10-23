from flask import Flask, render_template, request, redirect
import sqlite3
import logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO)

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS expenses 
                 (id INTEGER PRIMARY KEY, title TEXT, amount REAL, category TEXT, date TEXT)''')
    conn.close()
init_db()

@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    expenses = conn.execute("SELECT * FROM expenses").fetchall()
    conn.close()
    total = sum([e[2] for e in expenses]) if expenses else 0
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add():
    try:
        title = request.form['title']
        amount = float(request.form['amount'])
        category = request.form['category']
        date = datetime.now().strftime("%Y-%m-%d")
        conn = sqlite3.connect('database.db')
        conn.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?,?,?,?)",
                     (title, amount, category, date))
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f"Error: {e}")
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    conn.execute("DELETE FROM expenses WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')
