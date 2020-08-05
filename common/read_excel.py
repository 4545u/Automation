# 导包 import xlrd
# 打开文件 book = xlrd.open_workbook(filename)
# 打开工作表 sheet = book.sheet_by_name(sheet_name)
# 读取工作表属性信息  rows = sheet.nrows
#                   cols = sheet.ncols
#                   name = sheet.name

# 读取工作表中的内容（读取一行，一列，一个单元格）
# row_values(rowx = index_num)
# col_values(colx = index_num)
# cell(rowx,colx).value

import xlrd


class ExcelUnit():
    #读取excel数据 行
    @staticmethod
    def read_excel_line(excel_path,sheet_name):
        xls = xlrd.open_workbook(excel_path)
        sheet = xls.sheet_by_name(sheet_name)
        dataList = []
        for line in range(1,sheet.nrows):
            tempList = [sheet.cell_value(line, 0), sheet.cell_value(line, 1), sheet.cell_value(line, 2)]
            dataList.append(tempList)
        return dataList

    @staticmethod
    def read_excel_rank(excel_path,sheet_name):
        xls = xlrd.open_workbook(excel_path)
        sheet = xls.sheet_by_name(sheet_name)
        datalist = []
        for rank in range(0,sheet.ncols):
            data_temp = [sheet.cell_value(1,rank),sheet.cell_value(2,rank),sheet.cell_value(3,rank)]
            datalist.append(data_temp)
        return datalist

    @staticmethod
    def read_excel_all(excel_path,sheet_name):
        xls = xlrd.open_workbook(excel_path)
        sheet = xls.sheet_by_name(sheet_name)
        data_list = []
        for line in range(1,sheet.nrows):
            data_rank = []
            for rank in range(1,sheet.ncols):
                data_rank.append(sheet.cell_value(line,rank))
            data_list.append(data_rank)
        return data_list

    @staticmethod
    # line 行   rank 列
    def read_excel_port(excel_path, sheet_name, start_line, end_line, start_rank, end_rank):
        xls = xlrd.open_workbook(excel_path)
        sheet = xls.sheet_by_name(sheet_name)
        data_list = []
        for line in range(start_line - 1, end_line):
            data_rank = []
            for rank in range(start_rank - 1, end_rank):
                data_rank.append(sheet.cell_value(line, rank))
            data_list.append(data_rank)
        return data_list