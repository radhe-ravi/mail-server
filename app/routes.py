from flask import Blueprint, request, jsonify
import os
import smtplib
from email.message import EmailMessage

email_bp = Blueprint('email', __name__) 

@email_bp.route('/api/send-email', methods=['POST'])
def send_email():
    try:
        to_email = request.form.get('to')
        subject = request.form.get('subject')
        body = request.form.get('body')
        attachment = request.files.get('attachment')  # file upload

        if not all([to_email, subject, body]):
            return jsonify({"error": "Missing one or more required fields"}), 400

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = os.environ['GMAIL_USER']
        msg['To'] = to_email
        msg.set_content(body)

        if attachment:
            file_data = attachment.read()
            file_name = attachment.filename
            msg.add_attachment(
                file_data,
                maintype='application',
                subtype='octet-stream',
                filename=file_name
            )

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.environ['GMAIL_USER'], os.environ['GMAIL_PASS'])
            smtp.send_message(msg)

        return jsonify({"message": "Email sent successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
