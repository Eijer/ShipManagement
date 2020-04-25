# -*- coding: utf-8 -*-
import scrapy
import requests
import re
import json
import time,random
import urllib.parse
from ShipsManagementSystem.items import ShipsmanagementsystemItem
from scrapy.http import Request
from fake_useragent import UserAgent


# 根据url发送post请求
def searchShip(mmsi,option):
    ua = UserAgent(verify_ssl=False)        # 可随机生成一个user-agent
    headers = {
        'User-Agent': ua.random,
        'Referer':'http://www.shipxy.com/',
        'Cookie':'tc_TC=; _elane_shipfilter_type=%u8D27%u8239%2C%u96C6%u88C5%u7BB1%u8239%2C%u6CB9%u8F6E%2C%u5F15%u822A%u8239%2C%u62D6%u8F6E%2C%u62D6%u5F15%2C%u6E14%u8239%2C%u6355%u635E%2C%u5BA2%u8239%2C%u641C%u6551%u8239%2C%u6E2F%u53E3%u4F9B%u5E94%u8239%2C%u88C5%u6709%u9632%u6C61%u88C5%u7F6E%u548C%u8BBE%u5907%u7684%u8239%u8236%2C%u6267%u6CD5%u8247%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u533B%u7597%u8239%2C%u7B26%u540818%u53F7%u51B3%u8BAE%28Mob-83%29%u7684%u8239%u8236%2C%u62D6%u5F15%u5E76%u4E14%u8239%u957F%3E200m%u6216%u8239%u5BBD%3E25m%2C%u758F%u6D5A%u6216%u6C34%u4E0B%u4F5C%u4E1A%2C%u6F5C%u6C34%u4F5C%u4E1A%2C%u53C2%u4E0E%u519B%u4E8B%u884C%u52A8%2C%u5E06%u8239%u822A%u884C%2C%u5A31%u4E50%u8239%2C%u5730%u6548%u5E94%u8239%2C%u9AD8%u901F%u8239%2C%u5176%u4ED6%u7C7B%u578B%u7684%u8239%u8236%2C%u5176%u4ED6; _elane_shipfilter_length=0%2C40%2C41%2C80%2C81%2C120%2C121%2C160%2C161%2C240%2C241%2C320%2C321%2C9999; _elane_shipfilter_sog=0%2C1; _filter_flag=-1; _elane_shipfilter_one=2; _elane_shipfilter_country=0%2C1%2C2; _elane_shipfilter_olength=; tc_QX=; _elane_maptype=MT_SEA; shipxy_v3_history_serch=s%u2606HAPPY%20HARRIER%u2606235515000%u260680%u2606MMSI%uFF1A235515000%7Cs%u2606TIRTA%20SAMUDRA%20XVII%u2606525015429%u260680%u2606MMSI%uFF1A525015429%7Cs%u2606ALPHA%20HAPPINESS%u2606240142000%u260670%u2606MMSI%uFF1A240142000%7Cs%u2606TOPEKA%u2606256657000%u260670%u2606MMSI%uFF1A256657000%7Cs%u2606H%20LEE%20WHITE%u2606366938770%u260670%u2606MMSI%uFF1A366938770%7Cs%u2606HANJIN%20PUNTA%20ARENAS%u2606211233290%u2606100%u2606MMSI%uFF1A211233290; FD857C2AF68165D4=tgqeQu5I/8346qkaNZk4sJH68UawfZWvy7POWo7LDkA9q4ORUkRpAHcDJZFrCNZ0bWnZNP/68yw=; Hm_lvt_adc1d4b64be85a31d37dd5e88526cc47=1587369039,1587389846,1587390883,1587536461; Hm_lpvt_adc1d4b64be85a31d37dd5e88526cc47=1587536466; SERVERID=ce54c768aca7be22386d8a7ce24ecdae|1587537375|1587536458'
    }
    # option=1时可请求靠港历史,option=0时可请求船舶详细数据
    if (option == 1):
        data = {'mmsi':mmsi,'btime':'1585051512','etime':'1587643512',type:'2'}
        baseUrl = 'http://www.shipxy.com/Ship/GetVoyage?'
    elif(option == 0):
        data = {'mmsi':mmsi}
        baseUrl = 'http://www.shipxy.com/Ship/GetShip?'
    # 将字典数据拼接到url中
    formData = urllib.parse.urlencode(data)
    baseUrl = baseUrl + formData
    time.sleep(0.5)
    response = requests.post(url=baseUrl, data=data, headers=headers)
    context = response.text
    context = json.loads(context)
    return context


# 把mmsi.txt的信息拼接到url中
def loadMmsi():
    mmsiFile = open('../GetMMSI/mmsi.txt','r')
    context = mmsiFile.readlines()
    urls = []
    for element in context:
        url = 'http://www.shipxy.com/Ship/GetSimilarShip?mmsi=' + element.strip()
        urls.append(url)
    return urls


# 重定义scrapy请求
def start_requests(self):
    ua = UserAgent(verify_ssl=False)
    for url in self.start_urls:
        headers={
            'User-Agent': ua.random,
            'Cookie':'tc_TC=; _elane_shipfilter_type=%u8D27%u8239%2C%u96C6%u88C5%u7BB1%u8239%2C%u6CB9%u8F6E%2C%u5F15%u822A%u8239%2C%u62D6%u8F6E%2C%u62D6%u5F15%2C%u6E14%u8239%2C%u6355%u635E%2C%u5BA2%u8239%2C%u641C%u6551%u8239%2C%u6E2F%u53E3%u4F9B%u5E94%u8239%2C%u88C5%u6709%u9632%u6C61%u88C5%u7F6E%u548C%u8BBE%u5907%u7684%u8239%u8236%2C%u6267%u6CD5%u8247%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u533B%u7597%u8239%2C%u7B26%u540818%u53F7%u51B3%u8BAE%28Mob-83%29%u7684%u8239%u8236%2C%u62D6%u5F15%u5E76%u4E14%u8239%u957F%3E200m%u6216%u8239%u5BBD%3E25m%2C%u758F%u6D5A%u6216%u6C34%u4E0B%u4F5C%u4E1A%2C%u6F5C%u6C34%u4F5C%u4E1A%2C%u53C2%u4E0E%u519B%u4E8B%u884C%u52A8%2C%u5E06%u8239%u822A%u884C%2C%u5A31%u4E50%u8239%2C%u5730%u6548%u5E94%u8239%2C%u9AD8%u901F%u8239%2C%u5176%u4ED6%u7C7B%u578B%u7684%u8239%u8236%2C%u5176%u4ED6; _elane_shipfilter_length=0%2C40%2C41%2C80%2C81%2C120%2C121%2C160%2C161%2C240%2C241%2C320%2C321%2C9999; _elane_shipfilter_sog=0%2C1; _filter_flag=-1; _elane_shipfilter_one=2; _elane_shipfilter_country=0%2C1%2C2; _elane_shipfilter_olength=; tc_QX=; _elane_maptype=MT_SEA; FD857C2AF68165D4=tgqeQu5I/8346qkaNZk4sJH68UawfZWvy7POWo7LDkA9q4ORUkRpAHcDJZFrCNZ0bWnZNP/68yw=; shipxy_v3_history_serch=s%u2606TOPEKA%u2606256657000%u260670%u2606IMO%uFF1A9211585%7Cs%u2606TOPEKA%u2606256657000%u260670%u2606MMSI%uFF1A256657000%7Cs%u2606HAPPY%20HARRIER%u2606235515000%u260680%u2606MMSI%uFF1A235515000%7Cs%u2606TIRTA%20SAMUDRA%20XVII%u2606525015429%u260680%u2606MMSI%uFF1A525015429%7Cs%u2606ALPHA%20HAPPINESS%u2606240142000%u260670%u2606MMSI%uFF1A240142000%7Cs%u2606H%20LEE%20WHITE%u2606366938770%u260670%u2606MMSI%uFF1A366938770%7Cs%u2606HANJIN%20PUNTA%20ARENAS%u2606211233290%u2606100%u2606MMSI%uFF1A211233290; Hm_lvt_adc1d4b64be85a31d37dd5e88526cc47=1587389846,1587390883,1587536461,1587565701; Hm_lpvt_adc1d4b64be85a31d37dd5e88526cc47=1587565760; SERVERID=8dac9e937b8701fba4cb1394cffade3e|1587565999|1587565699',
        }

        time.sleep(0.5)
        yield requests.get(url,headers=headers) 

# 以mmsi为种子生成随机数
def waitTime(mmsi):
    random.seed(int(mmsi))
    return(random.random.uniform(1,4))


class ShipsSpider(scrapy.Spider):
    name = 'ships'
    allowed_domains = ['shipxy.com']
    # 请求相应船舶的最多十个相似船舶mmsi代码
    start_urls = loadMmsi()

    # 解析mmsi
    def parse(self,response):
        mmsi = re.findall('"m":(.*?),',response.text)
        for element in mmsi:
            # 把mmsi和网址传进管道
            item = ShipsmanagementsystemItem()
            url='http://www.shipxy.com/Ship/GetSimilarShip?mmsi=' + element
            # 发起请求
            time.sleep(waitTime(element))
            yield Request(url=url,callback=self.detailParse)

    def detailParse(self, response):
        mmsi = re.findall('"m":(.*?),',response.text)
        # 船舶详细信息 关于变量名的解释详见上级文件夹中的items.py
        for element in mmsi:
            time.sleep(waitTime(element))
            item = ShipsmanagementsystemItem()      # 声明item类
            time.sleep(waitTime(element))
            data = searchShip(element,0)            # 爬取船舶信息
            item['mmsi']= data['data'][0]['mmsi']
            item['imo']= data['data'][0]['imo']
            item['shipType']= str(data['data'][0]['type'])
            item['name']= data['data'][0]['name']
            item['callsign']= data['data'][0]['callsign']
            item['length']= str(data['data'][0]['length'])
            item['width']= str(data['data'][0]['width'])
            item['draught']= str(data['data'][0]['draught'])
            item['dest']= data['data'][0]['dest']
            item['eta']= data['data'][0]['eta']
            item['lon']= str(data['data'][0]['lon'])
            item['lat']= str(data['data'][0]['lat'])
            item['sog']= str(data['data'][0]['sog'])
            item['cog']= str(data['data'][0]['cog'])
            item['hdg']= str(data['data'][0]['hdg'])
            item['navistatus']= str(data['data'][0]['navistatus'])
            time.sleep(0.5)
            historyData = searchShip(element,1)         # 爬取船舶靠港历史
            item['stayHistory']= historyData['data']
            nextUrl= 'http://www.shipxy.com/Ship/GetSimilarShip?mmsi=' + element
            yield Request(url=nextUrl,callback=self.parse,dont_filter=True)     # 再迭代一次
            yield item
