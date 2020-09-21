from pushshift_py import PushshiftAPI
api = PushshiftAPI()

import smtplib
import numpy as np
import pandas as pd
import time
import math

def estimate_location(reddit_username):
    q_gta = "Toronto|askTO|Brampton|GTA|Missisauga|Durham|Ontario|Niagara|Oakville"
    q_elsewhere = "Montreal|Calgary|Ottawa|Edmonton|Winnipeg|Vancouver|Quebec|Halifax"

    gen_gta = api.search_comments(q=q_gta, author=reddit_username)
    gen_elsewhere = api.search_comments(q=q_elsewhere, author=reddit_username)

    return("GTA posts: " + str(len(list(gen_gta))) + ", Elsewhere posts: " + str(len(list(gen_elsewhere))))

q_terms = "CAD"
result_matrix = pd.DataFrame({'subreddit': [ ], 'url': [], 'hours ago': [], 'location data': []})
result_size_max = 15
after_days = '1d'

def print_links_of_sub(sub, rmx):
    gen = api.search_submissions(size=result_size_max, subreddit=sub, q=q_terms, after=after_days,
                                 filter=['url','author', 'title', 'subreddit'], sort='desc', sort_type='created_utc')

    results = list(gen)
    for i in range(min(len(results), result_size_max)):
        rmx = rmx.append({'subreddit': results[i][2], 'url': results[i][4],
                          'hours ago': math.floor((int(time.time()) - results[i][1])/3600),
                          'location data': estimate_location(results[i][0])},
                         ignore_index=True, sort=False)
    return rmx

subs = ['whatcarshouldibuy', 'askcarguys', 'askcarsales', 'toyota',
        'honda', 'hyundai', 'ford', 'mazda', 'audi', 'lexus',
        'mercedes_benz', 'bmw', 'subaru', 'dodge', 'kia', 'nissan',
        'ferrari', 'porsche', 'corvette', 'mitsubishi', 'jaguar',
        'landrover', 'volvo', 'scion']

for i in range(len(subs)):
    result_matrix = print_links_of_sub(subs[i], result_matrix)

pd.options.display.max_colwidth = 700
result_matrix = result_matrix.sort_values(by='hours ago', ascending=True)

def send_email(recipient, message):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gmailUser = 'anew232519@gmail.com'
    gmailPassword = 'hunter2' #replace with your own password

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

send_email("jamiealizadeh@gmail.com", result_matrix.to_string())