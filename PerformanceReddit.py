from pushshift_py import PushshiftAPI
api = PushshiftAPI()

from campaign1 import campaign_1
from campaign2 import campaign_2

import smtplib
import numpy as np

import time
import math

if __name__ == "__main__":
    campaign_1()
    campaign_2()
    #campaign_3()