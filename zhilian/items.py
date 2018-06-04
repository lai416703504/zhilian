# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class ZhilianItem(Item):
    jobName = Field()
    jobUrl = Field()
    companyName = Field()
    companyUrl = Field()
    companySize = Field()
    companyNature = Field()
    salary = Field()
    maxSalary = Field()
    minSalary = Field()
    location = Field()
    deatil = Field()
    edu = Field()
    workYear = Field()
    pass
