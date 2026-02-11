from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config DB ====================================================
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning 

# db insance
db = SQLAlchemy(app)
class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reps = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)

def spawn_db():
    with app.app_context():
        db.create_all() # creates database

@app.route('/')
def index():
    reps = Workouts.query.all()
    return render_template('index.html')
    
@app.route('/add', methods=['POST'])   
def add():
    repsInput = request.form.get('repsInput')
    if repsInput.isdigit():
        wrk = Workouts(reps=repsInput)
        db.session.add(wrk)
        db.session.commit()
        return render_template('index.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    spawn_db()
    app.run()

