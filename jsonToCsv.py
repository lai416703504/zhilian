# -*- coding: utf-8 -*-

import json
import csv
from pandas import DataFrame

file = open('zhilian1.json')
joblist = []
for eachline in file:
    joblist.append(json.loads(eachline))

df = DataFrame(joblist)
df.to_csv(path_or_buf='zhilianAll.csv', encoding='utf-8',index=False)
