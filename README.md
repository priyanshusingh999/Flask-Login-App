# Flask-Login

## Description
Flask-Login is a Flask web application that provides user registration, login/logout functionality, password reset via email, and a contact form that sends messages via Telegram. It uses a simple SQLite database backend and integrates with Yandex email and Telegram for notifications.

## Features
- User registration with name, email, and password
- User login and session management
- Password reset via email (using Yandex email service)
- Contact form that sends messages to a Telegram chat
- Simple SQLite database for storing user information

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Flask-Login
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set the following environment variables:
   - `SECRET_KEY` : Secret key for Flask sessions
   - `EMAIL_ID` : Email ID for sending password reset emails (Yandex email)
   - `PASSWORD_ID` : Password for the email account
   - `TELEGRAM_BOT_TOKEN` : Telegram bot token for sending messages
   - `TELEGRAM_CHAT_ID` : Telegram chat ID to receive messages

   Example (Windows CMD):
   ```cmd
   set SECRET_KEY=your_secret_key
   set EMAIL_ID=your_email@example.com
   set PASSWORD_ID=your_email_password
   set TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   set TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://localhost:5000/
   ```

3. Use the web interface to register, log in, reset your password, or send messages via the contact form.

## Dependencies
- Flask
- Flask-SQLAlchemy

## Project Structure (Overview)
```
Flask-Login/
├── app.py               # Main Flask application
├── config.py            # Configuration and environment variables
├── requirements.txt     # Python dependencies
├── routes/              # Email and Telegram messaging routes
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates for the web pages
└── __pycache__/         # Python cache files
```

## License
This project is open source and free to use.
