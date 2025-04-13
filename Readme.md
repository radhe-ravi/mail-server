# Python Mail Server

A simple Python-based mail server that allows sending emails with attachments via a REST API. This project utilizes Flask for the API and SMTP for email sending through Gmail.

## Features

- Send email via a REST API.
- Attach files to the email.
- Supports HTML email bodies.
- Easily extendable with more features (like scheduled emails, CC/BCC support, etc.).

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.6+
- `pip` (Python package installer)
- Gmail account (for sending emails)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/radhe-ravi/mail-server.git
cd python-mail-server
```

### 2. Set up a virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure environment variables

Create a .env file in the root of the project directory with the following content:

GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password

    Note: If you are using Gmail, you need to create an "App Password" (due to Google's security requirements). You can follow the steps to create an app password here.

### 5. Run the server

Start the Flask server:

python run.py

By default, the server will run on http://localhost:5000.
API Usage
Send Email with Attachment

To send an email, use a POST request to /api/send-email with the following parameters:

    to: Recipient email address (string).

    subject: Email subject (string).

    body: Email body (string, can be HTML).

    attachment: File to be attached (path to the file).

Example using curl:

curl -X POST http://localhost:5000/api/send-email \
  -F "to=recipient@example.com" \
  -F "subject=Test Email" \
  -F "body=This is a test email with attachment." \
  -F "attachment=@/path/to/your/file.zip"

Response

On success, you will receive a response with HTTP status 200 and a message indicating that the email has been sent successfully.

{
  "message": "Email sent successfully."
}

If there is an error (e.g., invalid credentials, missing parameters), the response will contain an error message.
Troubleshooting

    Issue with authentication (Gmail): Make sure you've created an "App Password" in your Google account as Gmail blocks access to less secure apps.

    Missing or invalid parameters: Ensure that all required parameters (to, subject, body, and attachment) are included in the request.

    File size limitations: Gmail and other email providers may have file size limitations. Ensure your attachments don't exceed their limits.