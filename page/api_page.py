from common.read_excel import *


def get_api_case():
    data = ExcelUnit.read_excel_all('E://git//Automation//test_file//api_case.xlsx','Sheet1')
    print(data)
    return data


get_api_case()