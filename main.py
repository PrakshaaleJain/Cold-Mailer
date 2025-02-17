import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


# Email credentials
email = "recipient@email.com"  # Your email
password = "password"  # App password generated that can be created by going to https://myaccount.google.com/


# Email content
subject = "Test Email from Python"
body = "Hello, this is a test email sent using Python with attachment."
text = f"Subject: {subject}\n\n{body}"

with open("emails.txt", "r") as file:
    email_list = [l.strip() for l in file if l.strip()]  

# Setting up the SMTP server using smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)


# This commneted code is for sending email without attachment

# for recipient in email_list:
#     try:
#         server.sendmail(email, recipient, text)
#         print(f"Email successfully sent to {recipient}")
#     except Exception as e:
#         print(f"Failed to send email to {recipient}: {e}")


# The below code is for sending emails with attachment
# Comment the above code if email sent without attachment is needed

attachment_path = "path/to/attachment"  # Path to the attachment file
for recipient in email_list:
    msg = MIMEMultipart() # Creates an email that supports attachments
    msg["From"] = email
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain")) # Attaches the email body (plain text)

    if os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            part = MIMEBase("application", "octet-stream") # Prepare the file as an attachment
            part.set_payload(f.read())                     # Read the attachment file
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")  # Add header to the attachment
            msg.attach(part)
    else:
        print(f"Couldn't find attachment at path: {attachment_path}")

    server.sendmail(email, recipient, msg.as_string())
    print(f"Email sent successfully to {recipient}")



server.quit()
