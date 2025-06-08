from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from routes.yandmail import send_yandex_email
from routes.telegram import send_telegram_message
from config import SECRET_KEY
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = f'{SECRET_KEY}'

class Register_Info(db.Model):
    name = db.Column(db.String(15), nullable=False, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = Register_Info(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('website/register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Register_Info.query.filter_by(email=email, password=password).first()
        if user:
            session['user'] = email
            return redirect(url_for('home'))
        else:
            error = "Invalid email or password."
    return render_template('website/login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/forget', methods=['GET', 'POST'])
def forget():
    if request.method == 'POST':
        email = request.form['email']
        user = Register_Info.query.filter_by(email=email).first()
        if user:
            if send_yandex_email(email, user.password):
                print('Password reset email sent successfully.')
            else:
                print('Failed to send password reset email.')
        else:
            print('User not found.')
        return redirect(url_for('forget'))
    return render_template('website/forget.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    msg_time = time.strftime('%d %a %b %Y %H:%M:%S')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        if send_telegram_message(name, email, message, msg_time):
            print('Message sent successfully.')
        else:
            print('Failed to send message.')
        return redirect(url_for('login'))
    return render_template('website/contact.html')


@app.route('/home')
def home():
    if 'user' in session:
        return render_template('index.html')
    return render_template('website/login.html')


@app.route('/about')
def about():
    return render_template('website/about.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=7000)
