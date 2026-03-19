from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/shop/items/')
def catalog():
    return 'This is catalog'

@app.route('/shop/item/<int:item_id>')
def show_item(item_id):
    return f'Вы смотрите товар под номером {item_id}'

with app.test_request_context():
    print(url_for('catalog'))
    print(url_for('show_item', item_id=42))
    print(url_for('catalog', color='Red', size='XL'))
