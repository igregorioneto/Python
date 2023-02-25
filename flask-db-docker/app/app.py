from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def db():
  return sqlite3.connect('database.db')

def create_table():
  c = db()
  c.execute(
    '''
      CREATE TABLE IF NOT EXISTS tasks
      (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL
      );
    '''
  )
  c.close()

@app.route('/')
def list_task():
  c = db()
  cursor = c.cursor()
  cursor.execute('SELECT * FROM tasks;')
  tasks = cursor.fetchall()
  c.close()
  return render_template('list.html', tasks=tasks)



