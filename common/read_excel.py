import xlrd


class ExcelUtil:
    def __init__(self,excel_path,Sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(Sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rownum = self.table.nrows
        # 获取总列数
        self.colnum = self.table.ncols

    def dict_data(self):
        if self.rownum <= 1:
            print("总行数小于等于1")
        else:
            data_list = []
            for line in range(1, self.rownum):
                data_rank = []
                for rank in range(0, self.colnum):
                    data_rank.append(self.table.cell_value(line, rank))
                data_list.append(data_rank)
            return data_list

