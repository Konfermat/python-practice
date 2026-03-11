from flask import render_template, redirect, url_for, request, flash, Flask
from flask_login import login_required, current_user, login_user, logout_user 
from extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Car 

# --- ИНИЦИАЛИЗАЦИЯ ---
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///garage.db'
    app.config['SECRET_KEY'] = 'secret'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- МАРШРУТЫ (ROUTES) ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Имя пользователя занято')
            return redirect(url_for('register'))
            
        hashed_pw = generate_password_hash(password)
        
        new_user = User(username=username, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        
        flash('Неверный логин или пароль')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Показываем только машины текущего пользователя
    user_cars = current_user.cars
    return render_template('dashboard.html', cars=user_cars)    

# --- УПРАВЛЕНИЕ ГАРАЖОМ ---
@app.route('/add_car', methods=['GET', 'POST'])
@login_required # Добавлять машины может только вошедший пользователь
def add_car():
    if request.method == 'POST':
        # Получаем данные из формы add_car.html
        brand = request.form.get('brand')
        model = request.form.get('model')
        year = request.form.get('year')
        fuel_type = request.form.get('fuel_type')

        # Создаем новый объект машины
        # user_id берем автоматически из текущего пользователя
        new_car = Car(
            brand=brand, 
            model=model, 
            year=int(year), 
            fuel_type=fuel_type, 
            user_id=current_user.id
        )

        try:
            db.session.add(new_car)
            db.session.commit()
            flash('Машина успешно добавлена в гараж!')
            return redirect(url_for('dashboard'))
        except Exception as e:
            db.session.rollback()
            flash('Ошибка при сохранении данных.')

    return render_template('add_car.html')

@app.route('/delete_car/<int:car_id>')
@login_required
def delete_car(car_id):
    # Ищем машину и проверяем, что она принадлежит именно этому пользователю
    car = Car.query.filter_by(id=car_id, user_id=current_user.id).first_or_404()
    
    db.session.delete(car)
    db.session.commit()
    flash('Машина удалена.')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)

