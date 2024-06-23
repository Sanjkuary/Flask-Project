from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):  # Changed class name to PascalCase
    SNo = db.Column(db.Integer, primary_key=True)  # Fixed typo: Interger -> Integer
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Fixed typo: Datetime -> DateTime

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.title}"

@app.cli.command('create-db')
def create_db():
    """Create the database tables."""
    db.create_all()
    print("Database tables created.")

@app.route('/')
def test():
    return 'Thank you!'

@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/skills/')
def skills():
    return render_template('skills.html')

@app.route('/experience/')
def experience():
    return render_template('experience.html')

@app.route('/myweb/')
def myweb():
    return render_template('myweb.html')

if __name__ == '__main__':
    app.run(debug=True)

