# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import json
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import re

mpl.rcParams['font.size'] = 8
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.sans-serif'] = ['SimHei']
custom_font = mpl.font_manager.FontProperties(fname='msyh.ttf')

file = open('zhilian.json')
joblist = []
for eachline in file:
    joblist.append(json.loads(eachline))

df = DataFrame(joblist)

df1 = df[['workYear', 'salary', 'maxSalary', 'minSalary']]
# df1 = df[['location', 'salary', 'maxSalary', 'minSalary']]

avgList = []

for index in df1.index:
    if df1.loc[index].minSalary.isdigit() and df1.loc[index].maxSalary.isdigit():
        avgList.append((int(df1.loc[index].minSalary) + int(df1.loc[index].maxSalary)) / 2.)
    else:
        avgList.append(np.nan)
df1.insert(4, 'avg', avgList)

avgSalarys = df1.groupby(['workYear'])['avg'].mean()
# avgSalarys = df1.groupby(['location'])['avg'].mean()

avg_map = dict(avgSalarys)

avg_list = list(avgSalarys.index)

plt.figure('quyu')

# plt.add_subplot(121)
plt.title(u'薪资', fontproperties=custom_font)

xticks = np.arange(len(avg_map))

longQuyuName = avg_map.keys()
quyuName = []
for quyu in longQuyuName:
    quyuName.append(quyu.split('-')[-1])

number = [x for x in avg_map.values()]

bar_width = 0.5

bars = plt.bar(xticks, number, width=bar_width, edgecolor='none')

for x, y in zip(xticks, number):
    plt.text(x, y + 500, '%.02f' % y, ha='center', va='top')

plt.ylabel(u'平均月薪（K）', fontproperties=custom_font)
# plt.xlabel(u'行政区', fontproperties=custom_font)
plt.xlabel(u'工作年限', fontproperties=custom_font)
plt.xticks(xticks + bar_width / 2, quyuName)

# plt.(quyuName, fontproperties=custom_font)

plt.xlim(([bar_width / 2 - 0.5, len(avg_map)]))

# plt.ylim([0.0, 10000.0])
plt.ylim([0.0, 30000.0])

# plt.savefig("avg_salary.png", dpi=100)
plt.savefig("avg_salary_of_workyear.png", dpi=100)

plt.show()
# plt.show()

# district
