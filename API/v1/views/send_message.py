from flask import Blueprint, request, jsonify
from flask_mail import Message
from API.v1.views import app_views
from API.v1.views.mail import mail  # Import mail object directly

# Define route for sending email
@app_views.route('/send-email', methods=['POST'], strict_slashes=False)
def send_email():
    # Extract data from request
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    phone_number = data.get('phoneNumber')
    description = data.get('description')

    # Create email message
    msg = Message('New Message from RealEstateHub Contact Form',
                  sender='your-email@example.com',
                  recipients=['recipient@example.com'])
    msg.body = f"""
    Name: {first_name} {last_name}
    Email: {email}
    Phone Number: {phone_number}
    Description: {description}
    """

    # Try to send email
    try:
        mail.send(msg)  # Use mail object directly
        return jsonify({'success': True, 'message': 'Email sent successfully.'}), 200
    except Exception as e:
        print(f'Error sending email: {e}')
        return jsonify({'success': False, 'message': 'Failed to send email.'}), 500
