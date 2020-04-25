import requests
import re
import parsel
import traceback
import time
import pymongo
import random


# 获取mmsi信息
def search_mmsi(data_mmsi):
    # 确立目标url
    url = 'http://www.shipxy.com/Ship/GetSimilarShip?mmsi=' + str(data_mmsi)
    headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    response = requests.get(url, headers=headers)

    # 通过正则拿到船舶mmsi
    if response.status_code == 200:
        mmsi = re.findall('"m":(.*?),', response.text)
    else:
        print('mmsi : ' + data_mmsi +' 请求错误')
        # print(traceback.format_exc())
    return mmsi


# 将mmsi.txt存入数据库
def write_into_mongo(client,data_base,mmsi_name):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[client]
    mycol = mydb[data_base]
    mmsi_file = open(mmsi_name,'r')
    context = mmsi_file.readlines() # 读取mmsi.txt文件

    # 插入mmsi 如果不存在则插入，若已存在则无操作
    for line in context:
        document = {'mmsi' : line.strip('\n')}
        mycol.update_many(
            document,
            {'$setOnInsert': document},
            upsert = True
        )
    mmsi_file.close()



# 主函数	参数1为种子文件名，参数2为mmsi文件名
def collect_mmsi(seed_name,mmsi_name):
	mmsi = []
	seed_file = open(seed_name,'r')
	context = seed_file.readlines() # 读取seed.txt文件
	seed_file.close()

	index = int(context[0])              # seed.txt文件的第一行记录已爬取次数
	for line in context[1:]:
	    line = line.strip()
	    mmsi = mmsi + search_mmsi(line)         # 获取相似mmsi序列
	    time.sleep(random.randint(1,3)) # 每秒执行一次
	index = index + 1               # 爬取次数+1
	mmsi = list(set(mmsi))          # 对列表去重

	#将新的mmsi列表覆盖至seed.txt
	del(context[0])
	seed_file = open(seed_name,'w')
	seed_file.write(str(index) + '\n')
	for line in mmsi:
	    seed_file.write(line + '\n')
	seed_file.close()

	mmsi_file = open(mmsi_name,'a')
	mmsi = mmsi + context
	mmsi = list(set(mmsi))          # 对列表去重
	for line in mmsi:
	    line = line.strip()
	    mmsi_file.write(line + '\n')
	mmsi_file.close()

	# 每爬取3次数据，将数据存入库中 
	#if (index % 3 == 0):
	#    write_into_mongo("ShipsManage","test2","test2.txt")
	#    # 清空文件
	#    mmsi_file = open(mmsi_name,'w')
	#    mmsi_file.close()


collect_mmsi("seed.txt","mmsi.txt")
# collect_mmsi("test.txt","test2.txt")
