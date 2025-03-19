import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from extract_data import extract_data
from email.mime.base import MIMEBase  # Add this line
from email_body import create_email_body
from send_email import send_email
# Load environment variables from .env file
load_dotenv()

sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
subject = "Final-Year B.Tech Student Seeking Full-Time/Internship Roles in MLOps, Machine Learning & Cloud Technologies – Aditya Yadav"
def main():
    # Extract data
    df = extract_data()
    print(df)
    for index, row in df.iterrows():
        name = row['Name']
        company = row['Company']
        title = row['Title']
        receiver_email = row['Email']
        body = create_email_body(name, company, title)
        send_email(sender_email, sender_password, receiver_email, subject, body)
        print(f"Email sent to {name} at {company}!")
if __name__ == '__main__':
    main()