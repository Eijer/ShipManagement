# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from ShipsManagementSystem.items import ShipsmanagementsystemItem
import json


def searchShip(base_url,mmsi):
    # base_url = 'http://www.shipxy.com/ship/GetShip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Referer':'http://www.shipxy.com/',
        'Cookie':'tc_TC=; _elane_shipfilter_type=%u8D27%u8239%2C%u96C6%u88C5%u7BB1%u8239%2C%u6CB9%u8F6E%2C%u5F15%u822A%u8239%2C%u62D6%u8F6E%2C%u62D6%u5F15%2C%u6E14%u8239%2C%u6355%u635E%2C%u5BA2%u8239%2C%u641C%u6551%u8239%2C%u6E2F%u53E3%u4F9B%u5E94%u8239%2C%u88C5%u6709%u9632%u6C61%u88C5%u7F6E%u548C%u8BBE%u5907%u7684%u8239%u8236%2C%u6267%u6CD5%u8247%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u533B%u7597%u8239%2C%u7B26%u540818%u53F7%u51B3%u8BAE%28Mob-83%29%u7684%u8239%u8236%2C%u62D6%u5F15%u5E76%u4E14%u8239%u957F%3E200m%u6216%u8239%u5BBD%3E25m%2C%u758F%u6D5A%u6216%u6C34%u4E0B%u4F5C%u4E1A%2C%u6F5C%u6C34%u4F5C%u4E1A%2C%u53C2%u4E0E%u519B%u4E8B%u884C%u52A8%2C%u5E06%u8239%u822A%u884C%2C%u5A31%u4E50%u8239%2C%u5730%u6548%u5E94%u8239%2C%u9AD8%u901F%u8239%2C%u5176%u4ED6%u7C7B%u578B%u7684%u8239%u8236%2C%u5176%u4ED6; _elane_shipfilter_length=0%2C40%2C41%2C80%2C81%2C120%2C121%2C160%2C161%2C240%2C241%2C320%2C321%2C9999; _elane_shipfilter_sog=0%2C1; _filter_flag=-1; _elane_shipfilter_one=2; _elane_shipfilter_country=0%2C1%2C2; _elane_shipfilter_olength=; tc_QX=; _elane_maptype=MT_SEA; shipxy_v3_history_serch=s%u2606HAPPY%20HARRIER%u2606235515000%u260680%u2606MMSI%uFF1A235515000%7Cs%u2606TIRTA%20SAMUDRA%20XVII%u2606525015429%u260680%u2606MMSI%uFF1A525015429%7Cs%u2606ALPHA%20HAPPINESS%u2606240142000%u260670%u2606MMSI%uFF1A240142000%7Cs%u2606TOPEKA%u2606256657000%u260670%u2606MMSI%uFF1A256657000%7Cs%u2606H%20LEE%20WHITE%u2606366938770%u260670%u2606MMSI%uFF1A366938770%7Cs%u2606HANJIN%20PUNTA%20ARENAS%u2606211233290%u2606100%u2606MMSI%uFF1A211233290; FD857C2AF68165D4=tgqeQu5I/8346qkaNZk4sJH68UawfZWvy7POWo7LDkA9q4ORUkRpAHcDJZFrCNZ0bWnZNP/68yw=; Hm_lvt_adc1d4b64be85a31d37dd5e88526cc47=1587369039,1587389846,1587390883,1587536461; Hm_lpvt_adc1d4b64be85a31d37dd5e88526cc47=1587536466; SERVERID=ce54c768aca7be22386d8a7ce24ecdae|1587537375|1587536458'
    }
    formdata = {
        # 'shipIDs': '235515000',
        'mmsi':mmsi
    }
    response = requests.post(url=base_url, data=formdata, headers=headers)
    data = response.text
    data = json.loads(data)
    return data

def start_requests(self):
    for url in self.start_urls:
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Cookie':'tc_TC=; _elane_shipfilter_type=%u8D27%u8239%2C%u96C6%u88C5%u7BB1%u8239%2C%u6CB9%u8F6E%2C%u5F15%u822A%u8239%2C%u62D6%u8F6E%2C%u62D6%u5F15%2C%u6E14%u8239%2C%u6355%u635E%2C%u5BA2%u8239%2C%u641C%u6551%u8239%2C%u6E2F%u53E3%u4F9B%u5E94%u8239%2C%u88C5%u6709%u9632%u6C61%u88C5%u7F6E%u548C%u8BBE%u5907%u7684%u8239%u8236%2C%u6267%u6CD5%u8247%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u533B%u7597%u8239%2C%u7B26%u540818%u53F7%u51B3%u8BAE%28Mob-83%29%u7684%u8239%u8236%2C%u62D6%u5F15%u5E76%u4E14%u8239%u957F%3E200m%u6216%u8239%u5BBD%3E25m%2C%u758F%u6D5A%u6216%u6C34%u4E0B%u4F5C%u4E1A%2C%u6F5C%u6C34%u4F5C%u4E1A%2C%u53C2%u4E0E%u519B%u4E8B%u884C%u52A8%2C%u5E06%u8239%u822A%u884C%2C%u5A31%u4E50%u8239%2C%u5730%u6548%u5E94%u8239%2C%u9AD8%u901F%u8239%2C%u5176%u4ED6%u7C7B%u578B%u7684%u8239%u8236%2C%u5176%u4ED6; _elane_shipfilter_length=0%2C40%2C41%2C80%2C81%2C120%2C121%2C160%2C161%2C240%2C241%2C320%2C321%2C9999; _elane_shipfilter_sog=0%2C1; _filter_flag=-1; _elane_shipfilter_one=2; _elane_shipfilter_country=0%2C1%2C2; _elane_shipfilter_olength=; tc_QX=; _elane_maptype=MT_SEA; FD857C2AF68165D4=tgqeQu5I/8346qkaNZk4sJH68UawfZWvy7POWo7LDkA9q4ORUkRpAHcDJZFrCNZ0bWnZNP/68yw=; shipxy_v3_history_serch=s%u2606TOPEKA%u2606256657000%u260670%u2606IMO%uFF1A9211585%7Cs%u2606TOPEKA%u2606256657000%u260670%u2606MMSI%uFF1A256657000%7Cs%u2606HAPPY%20HARRIER%u2606235515000%u260680%u2606MMSI%uFF1A235515000%7Cs%u2606TIRTA%20SAMUDRA%20XVII%u2606525015429%u260680%u2606MMSI%uFF1A525015429%7Cs%u2606ALPHA%20HAPPINESS%u2606240142000%u260670%u2606MMSI%uFF1A240142000%7Cs%u2606H%20LEE%20WHITE%u2606366938770%u260670%u2606MMSI%uFF1A366938770%7Cs%u2606HANJIN%20PUNTA%20ARENAS%u2606211233290%u2606100%u2606MMSI%uFF1A211233290; Hm_lvt_adc1d4b64be85a31d37dd5e88526cc47=1587389846,1587390883,1587536461,1587565701; Hm_lpvt_adc1d4b64be85a31d37dd5e88526cc47=1587565760; SERVERID=8dac9e937b8701fba4cb1394cffade3e|1587565999|1587565699',
        }
        yield requests.get(url,headers=headers) 

class ShipsSpider(scrapy.Spider):
    name = 'ships'
    allowed_domains = ['http://www.shipxy.com']
    start_urls = ['http://www.shipxy.com/Ship/GetSimilarShip?mmsi=256657000']

    def parse(self, response):
        mmsi = re.findall('"m":(.*?),',response.text)
        detailUrl = 'http://www.shipxy.com/Ship/GetShip'
        for element in mmsi:
            data = searchShip(detailUrl,element)
            item = ShipsmanagementsystemItem()
            item['mmsi']= data['data'][0]['mmsi']
            item['imo']= data['data'][0]['imo']
            item['shipType']= data['data'][0]['type']
            item['name']= data['data'][0]['name']
            item['callsign']= data['data'][0]['callsign']
            item['length']= data['data'][0]['length']
            item['width']= data['data'][0]['width']
            item['draught']= data['data'][0]['draught']
            item['dest']= data['data'][0]['dest']
            item['eta']= data['data'][0]['eta']
            item['lon']= data['data'][0]['lon']
            item['lat']= data['data'][0]['lat']
            item['sog']= data['data'][0]['sog']
            item['cog']= data['data'][0]['cog']
            item['hdg']= data['data'][0]['hdg']
            item['navistatus']= data['data'][0]['navistatus']
            yield item
