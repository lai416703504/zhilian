# -*- coding: utf-8 -*-
import scrapy
from zhilian.items import ZhilianItem
import uuid
import re


def get_uuid():
    return str(uuid.uuid4())


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://www.zhaopin.com/']

    kd = 'java'
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw='+ kd +'&p='
    cookie = "JSESSIONID=" + get_uuid() + ";" \
                                          "user_trace_token=" + get_uuid() + "; LGUID=" + get_uuid() + "; index_location_city=%E6%88%90%E9%83%BD; " \
                                                                                                       "SEARCH_ID=" + get_uuid() + '; _gid=GA1.2.717841549.1514043316; ' \
                                                                                                                                   '_ga=GA1.2.952298646.1514043316; ' \
                                                                                                                                   'LGSID=' + get_uuid() + "; " \
                                                                                                                                                           "LGRID=" + get_uuid() + "; "

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_ga=GA1.2.1675705296.1525503483; user_trace_token=20180505145804-a854ed80-5031-11e8-869c-525400f775ce; LGUID=20180505145804-a854f0b2-5031-11e8-869c-525400f775ce; _gid=GA1.2.1639933130.1525856914; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAABAACEBACDG04FABB7BD87B79FAC311DCA849B647AD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525503484,1525869827; X_HTTP_TOKEN=a182ed869a8003910c5f297e88d8d0ce; X_MIDDLE_TOKEN=08efdfbc4e46f32d79b4965ed35ed919; LGSID=20180510142346-b222b4ee-541a-11e8-81e3-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525938024; LGRID=20180510154024-663ed077-5425-11e8-93e9-525400f775ce; TG-TRACK-CODE=search_code; SEARCH_ID=be579ebfc13249c4b2dfbcef8a093f71',
        'Cookie': cookie,
        'Host': 'sou.zhaopin.com',
        'Origin': 'https://www.zhaopin.com',
        'Referer': 'https://www.zhaopin.com/',
        'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'}

    def start_requests(self):

        yield scrapy.Request(self.url + str(1), method='GET',
                             meta={'p': 1}, headers=self.headers, callback=self.parse)

    def parse(self, response):
        totalCount = response.xpath("/html/body/div[3]/div[3]/div[2]/span[1]/em/text()").extract()[0]

        pages = int(int(totalCount) / 60)

        if pages >= 100:
            pages = 100
        else:
            pages = pages

        for result in response.xpath('//*[@id="newlist_list_content_table"]/table')[1:]:
            item = ZhilianItem()
            try:
                item['jobName'] = result.xpath('.//tr[1]/td[1]/div/a/text()').extract()[0]
            except Exception as e:
                item['jobName'] = ''

            try:
                item['jobUrl'] = result.xpath('.//tr[1]/td[1]/div/a/@href').extract()[0]
            except Exception as e:
                item['jobUrl'] = ''

            try:
                item['companyName'] = result.xpath('.//tr[1]/td[3]/a[1]/text()').extract()[0]
            except Exception as e:
                item['companyName'] = ''

            try:
                item['companyUrl'] = result.xpath('.//tr[1]/td[3]/a[1]/@href').extract()[0]
            except Exception as e:
                item['companyUrl'] = ''
            try:
                item['companySize'] = (result.xpath(u'.//tr[2]/td/div/div/ul/li[1]//span[contains(text(),"公司规模")]/text()').extract()[0]).replace(u'公司规模：', '')
            except Exception as e:
                item['companySize'] = ''
            try:
                item['companyNature'] = (result.xpath(u'.//tr[2]/td/div/div/ul/li[1]//span[contains(text(),"公司性质")]/text()').extract()[0]).replace(u'公司性质：', '')
            except Exception as e:
                item['companyNature'] = ''

            try:
                item['salary'] = result.xpath('.//tr[1]/td[4]/text()').extract()[0]
                salaryList = re.split('-', item['salary'])
                item['minSalary'] = salaryList[0]
                item['maxSalary'] = salaryList[1]
            except Exception as e:
                item['salary'] = ''
                item['minSalary'] = ''
                item['maxSalary'] = ''

            try:
                item['location'] = result.xpath('.//tr[1]/td[5]/text()').extract()[0]
            except Exception as e:
                item['location'] = ''

            try:
                item['deatil'] = result.xpath('.//tr[2]/td/div/div/ul/li[2]/text()').extract()[0]
            except Exception as e:
                item['deatil'] = ''

            try:
                item['edu'] = (result.xpath(u'.//tr[2]/td/div/div/ul/li[1]//span[contains(text(),"学历")]/text()').extract()[0]).replace(u'学历：', '')
            except Exception as e:
                item['edu'] = ''

            try:
                item['workYear'] = (result.xpath(u'.//tr[2]/td/div/div/ul/li[1]//span[contains(text(),"经验")]/text()').extract()[0]).replace(u'经验：', '')
            except Exception as e:
                item['workYear'] = ''
            yield item

        p = int(response.meta.get('p')) + 1
        if p <= pages:
            yield scrapy.Request(self.url + str(p),
                                 method='GET', meta={'p': p}, headers=self.headers, callback=self.parse)
