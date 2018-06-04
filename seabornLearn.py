# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats, integrate

#
# def sinplot(flip=1):
#     x = np.linspace(0, 14, 100)
#     for i in range(1, 7):
#         plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
#
#
# with sns.axes_style("darkgrid"):
#     plt.subplot(211)
#     sinplot()
#
# plt.subplot(212)
# sinplot(-1)
# plt.show()

# x = np.random.normal(size=100)
# # sns.distplot(x, bins=20, hist=False, rug=True)
# sns.kdeplot(x, shade=True)
# plt.show()

# x = np.random.normal(0, 1, size=30)
# sns.kdeplot(x)
# sns.kdeplot(x, bw=.2, label='bw:0.2')
# sns.kdeplot(x, bw=2, label='bw:2')
# plt.show()


# x = np.random.gamma(6, size=200)
# sns.distplot(x, kde=False, fit=stats.gamma)
# plt.show()


# mean, cov = [0, 1], [(1, .5), (.5, 1)]
# data = np.random.multivariate_normal(mean, cov, 200)
# df = pd.DataFrame(data, columns=['x', 'y'])
# # print df
# sns.jointplot(x='x', y='y', data=df)
# plt.show()


# mean, cov = [0, 1], [(1, .5), (.5, 1)]
# x, y = np.random.multivariate_normal(mean, cov, 1000).T
# sns.jointplot(x=x, y=y, kind='hex')
# plt.show()

# mean, cov = [0, 1], [(1, .5), (.5, 1)]
# data = np.random.multivariate_normal(mean, cov, 200)
# df = pd.DataFrame(data, columns=['x', 'y'])
# sns.jointplot(x='x', y='y', data=df, kind='kde')
# plt.show()

# mean, cov = [0, 1], [(1, .5), (.5, 1)]
# data = np.random.multivariate_normal(mean, cov, 200)
# df = pd.DataFrame(data, columns=['x', 'y'])
# f, ax = plt.subplots(figsize=(6, 6))
# sns.kdeplot(df.x, df.y, ax=ax)
# sns.rugplot(df.x, color='g', ax=ax)
# sns.rugplot(df.y, vertical=True, ax=ax)
# plt.show()

# mean, cov = [0, 1], [(1, .5), (.5, 1)]
# data = np.random.multivariate_normal(mean, cov, 200)
# df = pd.DataFrame(data, columns=['x', 'y'])
# f, ax = plt.subplots(figsize=(6, 6))
# cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
# sns.kdeplot(df.x, df.y, cmap=cmap, n_levels=60, shade=True)
# plt.show()

sns.set(style='whitegrid', color_codes=True)
np.random.seed(sum(map(ord, "categorical")))
tips = sns.load_dataset("tips")
titanic = sns.load_dataset('titanic')
iris = sns.load_dataset('iris')
# palette 调色板
# 分组绘制箱线图，分组因子是day，在x轴不同位置绘制
# 分组箱线图，分子因子是time，不同的因子用不同颜色区分
# 相当于分组之后又分组
print tips
# sns.boxplot(y="total_bill", x="day", hue="time", data=tips)
# plt.show()
