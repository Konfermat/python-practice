from datetime import datetime
from flask import render_template, url_for, flash, redirect, jsonify, Blueprint
from flask_login import current_user,login_required, login_user, logout_user
from .models import User, Doctor, Patient, Specialization, Procedure, Appointment
from .forms import RegistrationForm, LoginForm, AppointmentForm
from .extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    form.specialization.choices = [(s.id, s.name) for s in Specialization.query.all()]
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            name=form.name.data,
            role=form.role.data
        )
        db.session.add(user)
        db.session.commit()

        if user.role == 'doctor':
            spec_id = form.specialization.data
            doc_name = form.name.data
            doctor = Doctor(
                name=doc_name,
                user_id = user.id,
                specialization_id = spec_id
            )
            db.session.add(doctor)
            db.session.commit()
        elif user.role == 'patient':
            name = form.name.data
            patient = Patient(
                name=name,
                user_id=user.id
            )
            db.session.add(patient)
            db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('main.login'))
    return  render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    pass

@main.route('/logout')
def logout():
    pass

@main.route('/dashboard')
@login_required
def dashboard():
    pass

@main.route('/appointment', methods=['GET', 'POST'])
@login_required
def appointment():
    pass
