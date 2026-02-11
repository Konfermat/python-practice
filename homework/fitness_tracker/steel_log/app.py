from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///workouts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reps = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


@app.route("/", methods=["GET", "POST"])
def index():
    # Добавление новой записи
    if request.method == "POST":
        try:
            reps = int(request.form["reps"])
            if reps < 0:
                raise ValueError()
            workout = Workout(reps=reps)
            db.session.add(workout)
            db.session.commit()
        except (ValueError, KeyError):
            pass  # игнорируем некорректный ввод

        return redirect(url_for("index"))

    # Чтение всех записей (новые сверху)
    workouts = Workout.query.order_by(Workout.date.desc()).all()
    
    # Временная зона
    dt2 = time.time()

    # Общая сумма повторений
    total_reps = sum(w.reps for w in workouts)

    return render_template("index.html", 
        workouts=workouts, 
        total_reps=total_reps,
        dt2=dt2,
        )


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
