from flask import Flask, request, url_for, redirect, render_template_string
from flask_mail import Mail, Message
from itsdangerous import URLSafeSerializer, BadSignature, SignatureExpired
import os

from app_instance import app

app.config['Mail Server'] = 'smtp.gmail.com'
app.config['Mail_PORT'] = 587
app.config['Mail_Use_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

# Secret key for token generation
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key')   

mail = Mail(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# ------------------ ROUTES ------------------

@app.route('/no')
def index():
    return '<a href="/send-verification?email=test@example.com">Send Verification Email</a>'

@app.route('/send-verification')
def send_verification():
    email = request.args.get('email')
    if not email:
        return "Email is required", 400

    # Generate a token valid for 1 hour
    token = serializer.dumps(email, salt='email-confirm')
    confirm_url = url_for('confirm_email', token=token, _external=True)

    # Send email
    try:
        msg = Message("Confirm Your Email", recipients=[email])
        msg.body = f"Click the link to verify your email: {confirm_url}"
        mail.send(msg)
    except Exception as e:
        return f"Error sending email: {e}", 500

    return f"Verification email sent to {email}"

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        # Token expires in 3600 seconds (1 hour)
        email = serializer.loads(token, salt='email-confirm', max_age=3600)
    except SignatureExpired:
        return "The confirmation link has expired.", 400
    except BadSignature:
        return "Invalid confirmation token.", 400

    # Here you would update the database to mark the email as verified
    return f"Email {email} has been verified successfully!"

# ------------------ MAIN ------------------
if __name__ == '__main__':
    app.run(debug=True)