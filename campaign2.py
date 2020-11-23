from pushshift_py import PushshiftAPI
api = PushshiftAPI()

from em import send_email
from returnLinksFromSub import print_links_of_sub
from estimateLocation import estimate_location

import pandas as pd
import math
import time

q_terms = "CAD|km|Toronto|askTO|Brampton|GTA|Missisauga|Durham|Ontario|Niagara|Oakville"
result_size_max = 15
after_days = '1d'

def cmpn2helper(sub, rmx):
    gen = api.search_submissions(size=result_size_max, subreddit=sub, after=after_days,
                                 filter=['url','author', 'title', 'subreddit'], sort='desc', sort_type='created_utc')

    results = list(gen)
    for i in range(min(len(results), result_size_max)):
        if estimate_location(results[i][0], postUpperLim=1)[11] != '0':
            rmx = rmx.append({'subreddit': results[i][2], 'url': results[i][4],
                            'hours ago': math.floor((int(time.time()) - results[i][1])/3600),
                            'location data': estimate_location(results[i][0])},
                            ignore_index=True, sort=False)
    return rmx

def campaign_2():
    result_matrix = pd.DataFrame({'subreddit': [ ], 'url': [], 'hours ago': [], 'location data': []})

    subs = ['whatcarshouldibuy']

    for i in range(len(subs)):
        result_matrix = cmpn2helper(subs[i], result_matrix)

    pd.options.display.max_colwidth = 700
    result_matrix = result_matrix.sort_values(by='hours ago', ascending=True)
    
    send_email("jamie.alizadeh@performance.ca", result_matrix.to_string())