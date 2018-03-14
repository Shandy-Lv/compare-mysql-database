import xlrd
import pymysql


def get_database_connection_from_excel(file_path):
    dic = get_database_info_from_excel(file_path)
    connection = pymysql.connect(host=dic["host"], user=dic["user"], passwd=dic["passwd"], database=dic["database"],
                                 port=int(dic["port"]), charset=dic["charset"])
    return connection


def get_database_info_from_excel(file_path):
    database_info_sheet = xlrd.open_workbook(file_path).sheets()[0]
    rows = database_info_sheet.nrows
    row = 0
    dic = {"": ""}
    while row < rows:
        dic[database_info_sheet.cell_value(row, 0)] = str(database_info_sheet.cell_value(row, 1))
        row += 1
    return dic

