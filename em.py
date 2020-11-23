import smtplib

def send_email(recipient, message):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gmailUser = 'anew232519@gmail.com'
    gmailPassword = 'Hunter2' #Not my real password

    msg = MIMEMultipart()
    msg['From'] = f'"Perf Leads" <{gmailUser}>'
    msg['To'] = recipient
    msg['Subject'] = "Daily Automated reddit.com Leads"
    msg.attach(MIMEText(message))

    try:
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmailUser, gmailPassword)
        mailServer.sendmail(gmailUser, recipient, msg.as_string())
        mailServer.close()
        print ('Email sent!')
    except:
        print ('Something went wrong...')