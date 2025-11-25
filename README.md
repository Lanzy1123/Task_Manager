```markdown
✅ Flask To-Do List App

A simple web-based To-Do List application built with Flask and Flask-SQLAlchemy using SQLite for data storage.

📌 Features

- Add, view, and delete tasks
- Stores tasks in an SQLite database
- Clean and responsive interface (HTML/CSS)
- Lightweight and beginner-friendly

🛠️ Tech Stack

- Python (Flask)
- SQLite (via Flask-SQLAlchemy)
- HTML/CSS (for frontend)

💻 Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

Install dependencies:

```bash
pip install flask flask_sqlalchemy
```

🚀 How to Run

1. Clone or download the project.
2. Run the app:

```bash
python main.py
```

3. Open your browser and visit:

```
http://127.0.0.1:5000/
```

🗂️ Project Structure

```
/project
│
├── main.py               # Flask application
├── templates/
│   └── index.html        # HTML template
├── static/
│   └── style.css         # Styling (optional)
└── README.md
```

🧠 Sample Code Snippet

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task = Task(content=request.form['content'])
        db.session.add(new_task)
        db.session.commit()
    tasks = Task.query.all()
  return render_template('index.html', tasks=tasks)
```

🧪 Future Improvements

- Mark tasks as completed
- Edit tasks
- User authentication

---

*Author:* *Lanzy1123*
