# import xlrd
# import xlwt
# from xlutils.copy import copy
# import xlutils
import requests
import re
import parsel
import traceback
import time

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
            mmsi = re.findall('"m":(.*?),', response.text)
            mmsi.append(str(data_mmsi))
    else:
        print('请求错误')
    return mmsi


# 用于在windows端将数据写入excel文件
def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    cols_old = worksheet.ncols# 获取表格中已存在的数据的列数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        new_worksheet.write(i, cols_old, value[i])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


# 读取seed.xlsx并写回文件
def load_mmsi_windows(filename): # filename = 'seed.xls'
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



mmsi = []
