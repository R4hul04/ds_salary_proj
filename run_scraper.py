<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:24:49 2023

@author: Rahul Parande
"""

import glassdoor_scrap as gs
import pandas as pd

path = "C:/Users/Rahul Parande/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15)
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:24:49 2023

@author: Rahul Parande
"""

import glassdoor_scrap as gs
import pandas as pd

path = "C:/Users/Rahul Parande/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15)
>>>>>>> fbf6b49b08c5c8784eb914a295564f5169402fa9
df.to_csv('glassdoor_jobs.csv', index = False)