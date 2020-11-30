from pushshift_py import PushshiftAPI
api = PushshiftAPI()

from em import send_email
from returnLinksFromSub import print_links_of_sub
from estimateLocation import estimate_location

import pandas as pd
import math
import time

q_t = "CAD|CDN|km|Abarth|Alfa|Aston|Audi|Bentley|BMW|Bugatti|Cadillac|Chevrolet|Chrysler|Citroen|Dacia|Daewoo|Daihatsu|Dodge|Donkervoort|DS|Ferrari|Fiat|Fisker|Ford|Honda|Hummer|Hyundai|Infiniti|Iveco|Jaguar|Jeep|Kia|KTM|Lada|Lamborghini|Lancia|Rover|Landwind|Lexus|Lotus|Maserati|Maybach|Mazda|McLaren|Mercedes-Benz|MG|Mini|Mitsubishi|Morgan|Nissan|Opel|Peugeot|Porsche|Renault|Rolls-Royce|Rover|Saab|Seat|Skoda|Smart|SsangYong|Subaru|Suzuki|Tesla|Toyota|Volkswagen|Volvo"
q_t += "Civic|Accord|Raptor|Mustang|Challenger|Highlander|Cruze|Elantra|Veloster"

def campaign_3():
    result_matrix = pd.DataFrame({'subreddit': [ ], 'url': [], 'hours ago': [], 'location data': []})

    subs = ['askTO', 'brampton', 'PersonalFinanceCanada']

    for i in range(len(subs)):
        result_matrix = print_links_of_sub(subs[i], result_matrix, q_terms=q_t, result_size_max=15, after_days='1d')

    pd.options.display.max_colwidth = 700
    result_matrix = result_matrix.sort_values(by='hours ago', ascending=True)
    
    send_email("jamie.alizadeh@performance.ca", result_matrix.to_string())