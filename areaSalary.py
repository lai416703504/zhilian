# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import DataFrame
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import re

mpl.rcParams['font.size'] = 8
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']
custom_font = mpl.font_manager.FontProperties(fname='msyh.ttf')

file = open('zhilian_net_huizhou.json')
joblist = []
for eachline in file:
    try:
        temp = json.loads(eachline)
    except Exception as e:
        temp = {}
    temp1 = {}
    if temp.has_key('maxSalary') and temp['maxSalary'].isdigit() and int(temp['maxSalary']) < 20000:
        pattern = r'(1-3)|(3-5)|(^$)'
        if re.match(pattern, temp['workYear'].encode('utf-8')):
            temp1['location'] = temp['location'].split('-')[-1]
            temp1['maxSalary'] = temp['maxSalary']
            temp1['workYear'] = temp['workYear']
            joblist.append(temp1)

        # pattern = r'(100-499)|(500-999)|(1000-9999)|(10000)'
        # if re.match(pattern, temp['companySize'].encode('utf-8')):
        #     temp1['location'] = temp['location'].split('-')[-1]
        #     temp1['maxSalary'] = temp['maxSalary']
        #     # temp1['workYear'] = temp['workYear']
        #     temp1['companySize'] = temp['companySize']
        #     joblist.append(temp1)

sns.set(style='whitegrid', color_codes=True, font=custom_font.get_name())

df = DataFrame(joblist)

df['maxSalary'] = df.maxSalary.astype(float)
df['location'] = df.location.astype(object)
df['workYear'] = df.workYear.astype(object)
# df['companySize'] = df.companySize.astype(object)

sns.boxplot(x="location", y="maxSalary", hue='workYear', data=df)
# sns.boxplot(x="location", y="maxSalary", hue='companySize', data=df)
plt.title('kuaiji')
plt.savefig("areaSalary_net_huizhou.png", dpi=100)

plt.show()
