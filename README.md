# 船舶管理系统（DEMO） #
- 本项目是一个信息管理系统。基于[船讯网](http://http://www.shipxy.com/)和[AIS信息服务平台](http://www.ais.msa.gov.cn/hsj/)上的船舶信息，管理和存储船舶在一段时间内产生的数据；描述船舶的各个状态；统计分析船舶中的数据。
- 该程序是项目的一个demo版本，作为获取船舶MMSI的一个测试。


## 第三方库 ##
- requests
- parsel(xpath)
- scrapy
- pymongo
## 开发环境 ##
- 使用语言：python3.7.6
## 大致思路 ##
## GetMMSI ##
1. 在地图上的不同区域采集不同种类的数个船舶的MMSI。
2. 根据船讯网的detail网页可以得到已知船舶的相似船舶，从而获取地图上的其他船舶的MMSI。
3. 有了船舶的MMSI后就可以在ais上获取到详细的船舶信息，例如船舶类型，呼号，吃水，经纬度等等。
## ShipsManagementSystem(SMS)##
1. 从之前的mmsi.txt文件中提取信息拼接到url中
2. 发送post请求提取信息
3. 将信息清洗并存入数据库中
