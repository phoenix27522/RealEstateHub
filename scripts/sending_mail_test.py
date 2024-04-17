from flask import Flask
from flask_mail import Mail, Message

# Create a Flask application context
app = Flask(__name__)

# Configure Flask-Mail with the same settings as in your Flask application
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kiflunahom1994@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'fylv nywq wiir vxfp'  # Your Gmail app password

# Initialize the Flask-Mail extension
mail = Mail(app)

# Function to send a test email
def send_test_email():
    with app.app_context():
        msg = Message(subject="Test Email",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=["recipient@example.com"])  # Replace with recipient's email address
        msg.body = "This is a test email sent from Flask-Mail."
        try:
            mail.send(msg)
            print("Test email sent successfully!")
        except Exception as e:
            print(f"Error sending test email: {e}")

# Call the send_test_email() function to send the test email
if __name__ == "__main__":
    send_test_email()
