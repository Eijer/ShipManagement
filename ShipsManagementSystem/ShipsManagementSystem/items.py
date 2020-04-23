# -*- coding= utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in=
# https=//doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShipsmanagementsystemItem(scrapy.Item):
    # define the fields for your item here like=
    # name = scrapy.Field()

    # 船舶信息
    mmsi=scrapy.Field()        # mmsi
    shipType=scrapy.Field()        # 船舶类型
    imo=scrapy.Field()             # imo
    name=scrapy.Field()            # 船名
    cnname=scrapy.Field()          # 船中文名
    callsign=scrapy.Field()        # 呼号
    length=scrapy.Field()          # 船长
    width=scrapy.Field()           # 船宽
    draught=scrapy.Field()         # 吃水
    dest=scrapy.Field()            # 目的地
    eta=scrapy.Field()             # 预到时间
    lon=scrapy.Field()             # 经度
    lat=scrapy.Field()             # 纬度 百万分之一度
    sog=scrapy.Field()             # 航速 百万分之一度
    cog=scrapy.Field()             # 航迹向
    hdg=scrapy.Field()             # 船首向
    navistatus=scrapy.Field()      # 航行状态
    rot=scrapy.Field()             # 旋转角速度
    satelliteutc=scrapy.Field()    # 航点时间
    shipId=scrapy.Field()
    tradeType=scrapy.Field()
    matchtype=scrapy.Field()
    left=scrapy.Field()
    trail=scrapy.Field()
    laststa=scrapy.Field()
    lastdyn=scrapy.Field()

    # 靠港信息
    stayHistory=scrapy.Field()
    #port=scrapy.Field()                 # 港口中文名
    #portEn=scrapy.Field()               # 港口英文名
    #ATA=scrapy.Field()                  # 到港时间
    #ATB=scrapy.Field()                  # 靠泊时间
    #ATD=scrapy.Field()                  # 离港时间
    #sailingTime=scrapy.Field()          # 航时(h)
    #countryCN=scrapy.Field()            # 国家或地区
    #distance=scrapy.Field()             # 航程(nm)
    #speed=scrapy.Field()                # 航速(kn)
    #stayInPort=scrapy.Field()           # 港口停留(h)
    #stayInTerminal=scrapy.Field()       # 码头作业(h)
    #waitBoTime=scrapy.Field()           # 等泊时间(h)
