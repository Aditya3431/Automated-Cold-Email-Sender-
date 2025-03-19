Automated Cold Email Sender for HR Outreach using Python
This project is designed to automate the process of sending personalized cold emails to HR professionals using Python. It extracts recipient details from a dataset, generates customized email content, and sends emails using SMTP with optional attachments like resumes.

🚀 Features
Automated Email Sending: Send bulk personalized emails.
Custom Email Templates: Dynamically generate email bodies using recipient information.
Attachment Support: Attach resumes or documents.
Environment Variables: Securely manage credentials using .env files.
Error Handling: Robust exception management for failed emails.
🛠️ Requirements
Python 3.x
smtplib
pandas
dotenv
email
os
You can install the necessary packages using:

bash
Copy
Edit
pip install -r requirements.txt
⚙️ Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your_username/cold-email-sender.git
cd cold-email-sender
Create a .env file and add your credentials:

env
Copy
Edit
SENDER_EMAIL=your_email@example.com
SENDER_PASSWORD=your_password
Place your email data in a CSV file (contacts.csv). Ensure it has columns:

Name
Email
Title
Company
Adjust the subject and template in the code as needed.

🚦 Usage
Run the program using the following command:

bash
Copy
Edit
python main.py
⚡ Example
Sends emails like:
vbnet
Copy
Edit
Subject: Excited to Connect with [Recipient's Name]
Dear [Recipient's Name],
I hope this message finds you well. I am enthusiastic about opportunities in MLOps, Machine Learning, and Cloud Technologies. 
Please find my resume attached for your review.
Best regards,
Aditya Yadav
🛡️ Security Note
Enable "Less secure apps" or create an App Password in Gmail for secure access.
Never share sensitive credentials or store them directly in your code.
🧑‍💻 Contributing
Contributions are welcome! Feel free to fork this repo, make changes, and submit a pull request.

📧 Contact
For any inquiries, reach out at aditya.7760@gmail.com.
