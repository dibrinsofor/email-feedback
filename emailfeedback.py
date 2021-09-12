import smtplib
import config
from email.message import EmailMessage
from datetime import date, datetime, time

file_with_potential_error = "simp.py"
today = date.today()
time = datetime.now()
the_time_is = time.time().strftime('%H:%M:%S')
error_msg = f"What's Gucci Bro,\n\n Take a look at {file_with_potential_error}. I just got word that it's down bad. It started bleeding at {the_time_is}. \ncheck up on it. read error logs and fix it. \n\n\n Shalom, \n not a bot but a brother that do be caring and shit."



def alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["to"] = to
    msg["subject"] = subject
    msg["from"] = config.USER

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config.USER, config.PASSWORD)
    server.send_message(msg)

    server.quit

# if you want to send text notifs instead of email then just find your carriers email attachmtnt like 023448589@verizon.net
if __name__ == "__main__":
    alert(f"Error in {file_with_potential_error}, {today}", error_msg, "dibrinsofor@gmail.com") 
