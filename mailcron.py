import fitz  # PyMuPDF
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Your email credentials
EMAIL_ADDRESS = "njatin3435@gmail.com"  # Replace with your email
EMAIL_PASSWORD = ""  # Use an App Password if using Gmail

def send_emails(to_email):
    subject = "Application for Software Engineer Position"
    body = """
    <html>
    <head>
        <style>
            body { color: black; font-family: Arial, sans-serif; }
            p { color: black; }
            ul { color: black; }
            li { color: black; }
        </style>
    </head>
    <body>
        <p>Dear HR Team,</p>
        <p>I hope you're doing well.</p>
        <p>My name is Jatin Narang, and I am currently a Software Engineer at Pratishthan Software Ventures, Bangalore. I am exploring new opportunities and would greatly appreciate it if you could consider referring me for any available fresher roles. I have hands-on experience with the following:</p>
        <ul>
            <li><strong>React and React Native</strong> for mobile and web application development</li>
            <li><strong>Node.js</strong> for backend development</li>
        </ul>
        <p>Here are my details for your reference:</p>
        <ul>
            <li><strong>Portfolio</strong>: <a href="https://movieu.netlify.app/">https://movieu.netlify.app/</a></li>
            <li><strong>Project</strong>: <a href="https://jatinnarang22.netlify.app/">https://jatinnarang22.netlify.app/</a></li>
            <li><strong>LinkedIn</strong>: <a href="https://www.linkedin.com/in/jatinnarang22/">https://www.linkedin.com/in/jatinnarang22/</a></li>
            <li><strong>GitHub</strong>: <a href="http://github.com/jatinnarang22">http://github.com/jatinnarang22</a></li>
            <li><strong>Resume</strong>: <a href="https://drive.google.com/file/d/1CVk5gsqAqOQz2vmn2Quyex_7Zw1gozOz/view?usp=drive_link">Google Drive Link</a></li>
        </ul>
        <p>Thank you for considering my application. I look forward to the possibility of discussing how my skills and enthusiasm for web development can contribute to your team.</p>
        <p>Best regards, <br><strong>Jatin Narang</strong> <br> Mobile: 9416544345</p>
    </body>
    </html>
    """

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def extract_emails_from_pdf(pdf_path):
    emails = set()
    doc = fitz.open(pdf_path)

    # Extract text and search for email addresses
    for page in doc:
        text = page.get_text("text")
        found_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        emails.update(found_emails)

    return list(emails)

# Example for testing
pdf_path = "hr_contacts.pdf"  # Replace with your actual PDF file
emails = extract_emails_from_pdf(pdf_path)

for email in emails:
    send_emails(email)
