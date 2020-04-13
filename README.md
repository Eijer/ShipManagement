# 船舶管理系统（DEMO） #
- 本项目是一个信息管理系统。项目在windows10平台上利用Pycharm开发，基于[船讯网](http://http://www.shipxy.com/)和[AIS信息服务平台](http://www.ais.msa.gov.cn/hsj/)上的船舶信息，管理和存储船舶在一段时间内产生的数据；描述船舶的各个状态；统计分析船舶中的数据。
- 该程序是项目的一个demo版本，作为获取船舶MMSI的一个测试。


## 第三方库##
- requests
- parsel(xpath)
## 开发环境 ##
- 版本：anaconda4.8.3(python3.7.6)
- 编辑器：pycharm 社区版
## 大致思路 ##
1. 在地图上的不同区域采集不同种类的数个船舶的MMSI。
2. 根据船讯网的detail网页可以得到已知船舶的相似船舶，从而获取地图上的其他船舶的MMSI。`代码中，通过request发送请求，每隔1分钟发送一个请求，数据结果存入库中`
3. 有了船舶的MMSI后就可以在ais上获取到详细的船舶信息，例如船舶类型，呼号，吃水，经纬度等等。

## 伪代码 ##
	import xxx
	
	#定义船的类
	class Ships():
		def _init_(self,mmsi)	#暂定一个参数

	#读取种子文件
	def load_seed(excel):
		mmsi= excel.data #将种子文件里的数据调入

	#请求船的办法
	def get_ship_in_db(self):
		data=[] 
		load_seed(excel)
		headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
		for i in mmsi:
			url ='http://www.shipxy.com/Ship/Detail?mmsi=" + str(mmsi)'
			response=requests.get(url, headers=headers)
			if response.status_code == 200 :
				try:
					sel = parsel.Selector(response.text)
	#将数据入库（暂时写入excel）
	def download_in_db(self,data_list):
	
	
	
	