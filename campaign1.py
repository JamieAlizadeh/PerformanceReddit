import pandas as pd
from em import send_email
from returnLinksFromSub import print_links_of_sub

def campaign_1():
    result_matrix = pd.DataFrame({'subreddit': [ ], 'url': [], 'hours ago': [], 'location data': []})

    subs = ['whatcarshouldibuy', 'askcarguys', 'askcarsales', 'toyota',
        'honda', 'hyundai', 'ford', 'mazda', 'audi', 'lexus',
        'mercedes_benz', 'bmw', 'subaru', 'dodge', 'kia', 'nissan',
        'ferrari', 'porsche', 'corvette', 'mitsubishi', 'jaguar',
        'landrover', 'volvo', 'scion', 'autos', 'cars']


    for i in range(len(subs)):
        result_matrix = print_links_of_sub(subs[i], result_matrix)

    pd.options.display.max_colwidth = 700
    result_matrix = result_matrix.sort_values(by='hours ago', ascending=True)

    send_email("jamie.alizadeh@performance.ca", result_matrix.to_string())