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
def list():
  c = db()
  cursor = c.cursor()
  cursor.execute('SELECT * FROM tasks;')
  tasks = cursor.fetchall()
  c.close()
  return render_template('list.html', tasks=tasks)

@app.route('/create', methods=['GET', 'POST'])
def create():
  if request.method == 'POST':
    title = request.form['title']
    description = request.form['description']
    c = db()
    cursor = c.cursor()
    cursor.execute('INSERT INTO tasks (title, description) values (?, ?)', (title, description))
    c.commit()
    c.close()
    return redirect(url_for('list'))
  return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
  c = db()
  cursor = c.cursor()
  cursor.execute('SELECT * FROM tasks WHERE id = ?', (id,))
  task = cursor.fetchone()
  if request.method == 'POST':
    title = request.form['title']
    description = request.form['description']
    cursor.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?', (title, description, id,))
    c.commit()
    c.close()
    return redirect(url_for('list'))
  c.close()
  return render_template('edit.html', task=task)

@app.route('/delete/<int:id>')
def remove(id):
  c = db()
  cursor = c.cursor()
  cursor.execute('DELETE FROM tasks WHERE id = ?', (id))
  return redirect(url_for(list))
