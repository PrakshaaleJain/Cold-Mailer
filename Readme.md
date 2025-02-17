# Bulk Email Sender with/without Attachment

This Python script allows you to send emails to multiple recipients listed in a text file. It supports sending emails with or without attachments using the SMTP protocol.

## Features
- Send bulk emails to multiple recipients.
- Supports attachments.
- Uses Gmail SMTP for email delivery.

## Prerequisites
Before running the script, ensure you have:
- A Gmail account.
- Enabled "Less Secure Apps" access or generated an App Password from your Google account settings ([Generate App Password](https://myaccount.google.com/)).
- Python3 installed on your system.

## Installation
1. Clone this repository:
   ```sh
   git clone git@github.com:PrakshaaleJain/Cold-Mailer.git
   cd Cold-Mailer
   ```
2. Create a virtual enviroment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate # on linux or MacOS
   venv\Scripts\activate # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install smtplib email os
   ```

## Configuration
1. Update the email credentials in the script:
   ```python
   email = "your-email@gmail.com"
   password = "your-app-password"
   ```
2. Add recipient email addresses in `emails.txt` (one per line).
3. Set the attachment file path:
   ```python
   attachment_path = "path/to/attachment"
   ```
4. Set the email file path:
   ```python
   with open("path/to/emails.txt", "r") as file:
      email_list = [l.strip() for l in file if l.strip()]
   ```

## Usage
Run the script using:
```sh
python3 send_email.py
```

## Notes
- Ensure your `emails.txt` file contains valid email addresses.
- If you do not want to send an attachment, comment out the relevant section in the script.
- Double-check the `attachment_path` to ensure the file exists before running the script.

## License
This project is licensed under the MIT License.

## Author
Your Name - [GitHub Profile](https://github.com/PrakshaaleJain)

