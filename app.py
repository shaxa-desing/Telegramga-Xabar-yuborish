from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_email():
    name = request.form['name']
    sender_email = request.form['email']
    message_text = request.form['message']

    receiver_email = "shahruhduschanov@gmail.com"  # <-- Sizning qabul qiluvchi emailingiz
    gmail_user = "shahruhduschanov@gmail.com"        # <-- Sizning Gmail
    gmail_app_password = "side dfxe tcjj drzm"      # <-- Gmail App Password

    subject = "Yangi xabar veb saytdan"

    # Email yaratish
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = receiver_email
    msg['Subject'] = subject

    body = f"Name: {name}\nEmail: {sender_email}\nMessage:\n{message_text}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(gmail_user, receiver_email, msg.as_string())
        server.quit()
        return "Xabar muvaffaqiyatli yuborildi!"
    except Exception as e:
        return f"Xabar yuborilmadi. Xatolik: {e}"

if __name__ == "__main__":
    app.run(debug=True)
