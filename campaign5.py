from pushshift_py import PushshiftAPI
api = PushshiftAPI()

from em import send_email
from estimateLocation import estimate_location

import pandas as pd
import math
import time

q_t = "Weekly - What Car Should I Buy Megathread"

def campaign_5():
    result_matrix = pd.DataFrame({'subreddit': [ ], 'url': [], 'hours ago': [], 'location data': []})
    
    result_matrix = print_links_of_sub(result_matrix, q_terms=q_t, result_size_max=8, after_days='36d')

    pd.options.display.max_colwidth = 700
    result_matrix = result_matrix.sort_values(by='hours ago', ascending=True)
    
    send_email("jamie.alizadeh@performance.ca", result_matrix.to_string())


def print_links_of_sub(rmx, **kwargs):
    gen = api.search_submissions(subreddit='cars', size=kwargs.get('result_size_max'), q=kwargs.get('q_terms'), after=kwargs.get('after_days'),
                                 filter=['url','author', 'title', 'subreddit', 'html_decode'], sort='desc', sort_type='created_utc')

    results = list(gen)

    for i in range(min(len(results), kwargs.get('result_size_max'))):
        rmx = rmx.append({'subreddit': results[i][2], 'url': results[i][4],
                        'hours ago': math.floor((int(time.time()) - results[i][1])/3600),
                        'location data': estimate_location(results[i][0])},
                        ignore_index=True, sort=False)
    return rmx