from email.mime.text import MIMEText
import smtplib
def email_send(email,height,average_height, count):
    from_email = "#############@gmail.com"
    from_password = "#### #### #### ####"
    to_email = email

    subject ="Height Data"
    message = "hey, tu peso es de </strong>%s</strong>, el promedio total es " \
    "           de</strong>%s</strong> de un total de </strong>%s</strong> personas." %(height,average_height,count)

    msg = MIMEText(message,"html")
    msg["subject"] = subject
    msg["to"] = to_email
    msg["From"] = from_email


    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)