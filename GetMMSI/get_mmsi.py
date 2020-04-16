import requests
import re
import parsel
import traceback
import time
import pymongo

# 建立船舶类
class Ships:
    def  __init__(self, mmsi):
        self.mmsi = str(mmsi)


# 获取mmsi信息
def search_mmsi(data_mmsi):
    # 确立目标url
    url = 'http://www.shipxy.com/Ship/GetSimilarShip?mmsi=' + str(data_mmsi)
    headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    response = requests.get(url, headers=headers)

    # 通过正则拿到船舶mmsi
    if response.status_code == 200:
            mmsi = mmsi + re.findall('"m":(.*?),', response.text)
    else:
        print('mmsi : ' + data_mmsi +' 请求错误')
        # print(traceback.format_exc())
    return mmsi


# 读取seed.txt并写入数据库
def load_mmsi(filename): # filename = 'seed.txt'
    seed_file = xlrd.open_workbook(filename)
    sheet = seed_file.sheet_by_name('Sheet1')
    col_new = sheet.ncols
    try:
        mmsi_lists = sheet.col_values(col_new-1)    # 读取到的数据为float类型
        mmsi_lists = [int(i) for i in mmsi_lists]   # 将列表元素转化为整型
        for mmsi_list in mmsi_lists:
            mmsi = mmsi + search_mmsi(mmsi_lists[col_new-1])
            time.sleep(0.5) # 每0.5秒执行一次

    except:
        print(traceback.format_exc())

    try:
        mmsi = list(set(mmsi))
        write_excel_xls_append(filename, mmsi)
    except:
        print(traceback.format_exc())

# 将mmsi.txt存入数据库
def write_into_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["ShipsManage"]
    mycol = mydb["ships"]
    mmsi_file = open("mmsi.txt",'rw')
    context = mmsi_file.readlines() # 读取mmsi.txt文件

    # 插入mmsi 如果不存在则插入，若已存在则无操作
    for line in context:
        document = {'mmsi' : str(line)}
        mycol.update_many(
            document,
            {'$setOnInsert': document},
            upsert = True
        )
    mmsi_file.close()




mmsi = []
seed_file = open('seed.txt')
mmsi_file = open("mmsi.txt",'a')
context = seed_file.readlines() # 读取seed.txt文件
index = context[0]              # seed.txt文件的第一行记录已爬取次数
for line in context[1:]:
    line = line.strip()
    # search_mmsi(line)         # 获取相似mmsi序列
index = index + 1               # 爬取次数+1
mmsi = list(set(mmsi))          # 对列表去重

#将新的mmsi列表覆盖至seed.txt
del(context[0])
seed_file.write(str(index) + '\n')
for line in mmsi:
    seed_file.write(line + '\n')
seed_file.close()

mmsi = mmsi + context
mmsi = list(set(mmsi))          # 对列表去重

for line in mmsi:
    mmsi_file.write(line + '\n')
mmsi_file.close()

# 每爬取3次数据，将数据存入库中 
if (index % 3 == 0):
    write_into_mongo()
    # 清空文件
    mmsi_file = open('mmsi.txt','w')
    mmsi_file.close()
