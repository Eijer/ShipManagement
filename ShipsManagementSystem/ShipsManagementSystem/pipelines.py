# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class ShipsmanagementsystemPipeline(object):
    def __init__(self):
        # 船舶数据处理
        self.shipType = '其他类型船舶'
        self.navistatus = '未知'
        #数据库相关信息
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        myclient = pymongo.MongoClient(host=host, port=port)    # 创建数据库链接
        mydb = myclient[dbname]         # 指定数据库
        self.post = mydb[sheetname]         # 指定表名
        #去重设置
        self.mmsi_set = set()


    def process_item(self, item, spider):
        if item['shipType']:
            if item['shipType']=='80' or item['shipType']=='85':
                item['shipType']='油轮'
            elif item['shipType']=='70' or item['shipType']=='71' :
                item['shipType']='货船'
            elif item['shipType']=='61' or item['shipType']=='60' or item['shipType']=='69':
                item['shipType']='客船'
            elif item['shipType']=='52':
                item['shipType']='拖轮'
            elif item['shipType']=='55':
                item['shipType']='娱乐船'
            elif item['shipType']=='30':
                item['shipType']='捕捞船'
            elif item['shipType']=='31':
                item['shipType']='拖引船'
            elif item['shipType']=='100':
                item['shipType']='集装箱船'
            elif item['shipType']=='33':
                item['shipType']='疏浚或水下作业'
            elif item['shipType']=='50':
                item['shipType']='引航船'
            else:
                item['shipType']=self.shipType
        else:
            item['shipType']=self.shipType

        if item['navistatus']:
            if item['navistatus']=='0':
                item['navistatus']='在航(主机推动)'
            elif item['navistatus']=='1':
                item['navistatus']='锚泊'
            elif item['navistatus']=='3':
                item['navistatus']='操作受限'
            elif item['navistatus']=='4':
                item['navistatus']='吃水受限'
            elif item['navistatus']=='5':
                item['navistatus']='靠泊'
            elif item['navistatus']=='8':
                item['navistatus']='靠船帆提供动力'
            else:
                item['navistatus']= self.navistatus
        else:
            item['navistatus']= self.navistatus

        # 将数据插入库中
        data = dict(item)
        self.post.insert(data)

        return item

    def process_item(self,item,spider):
        mmsi = item['mmsi']
        if mmsi in self.mmsi_set:
            raise DropItem("mmsi found:%s" % item)

        self.mmsi_set.add(mmsi)
        return item

