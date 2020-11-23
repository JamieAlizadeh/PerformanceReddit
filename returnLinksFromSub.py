from pushshift_py import PushshiftAPI
api = PushshiftAPI()

from estimateLocation import estimate_location

import pandas as pd
import math
import time

def print_links_of_sub(sub, rmx, **kwargs):
    gen = api.search_submissions(size=kwargs.get('result_size_max'), subreddit=sub, q=kwargs.get('q_terms'), after=kwargs.get('after_days'),
                                 filter=['url','author', 'title', 'subreddit'], sort='desc', sort_type='created_utc')

    results = list(gen)
    for i in range(min(len(results), kwargs.get('result_size_max'))):
        rmx = rmx.append({'subreddit': results[i][2], 'url': results[i][4],
                          'hours ago': math.floor((int(time.time()) - results[i][1])/3600),
                          'location data': estimate_location(results[i][0])},
                         ignore_index=True, sort=False)
    return rmx