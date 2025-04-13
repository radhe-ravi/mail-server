from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

@app.route('/api/send-email', methods=['POST'])
def send_email():
    to_email = request.form.get('to')
    subject = request.form.get('subject')
    body = request.form.get('body')
    attachment = request.files.get('attachment')

    if not to_email or not subject or not body:
        return jsonify({"error": "Missing required fields"}), 400

    # Prepare the email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = os.environ['GMAIL_USER']
    msg['To'] = to_email
    msg.set_content(body)

    # Attach file if present
    if attachment:
        file_data = attachment.read()
        file_name = attachment.filename
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.environ['GMAIL_USER'], os.environ['GMAIL_PASS'])
            smtp.send_message(msg)
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
