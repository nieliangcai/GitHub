import os
import yaml
from xlrd import open_workbook

class YamlReader(object):
    '''实现读取YML文件内容'''
    def __init__(self,yaml):
        if os.path.exists(yaml):
            self.yaml = yaml
        else:
            raise FileNotFoundError("请检查Config模块，是不是缺少了yml文件！")
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yaml,'rb') as f:
                self._data = list(yaml.safe_load_all(f))
            return self._data

class ExcelNotFoundError(Exception):
    pass
class SheetTypeError(Exception):
    pass

class ExcelReader(object):
    '''实现读取Excel功能'''
    def __init__(self,excel,sheet=0,title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise ExcelNotFoundError("请检查data中的Excel文件，是不是没有你设置的那个Excel文件!")
        self.sheet = sheet
        self.title = title_line
        self._data = list()

    @property
    def data(self):
        '''是否存在title栏，一般第一行为title;如果有title栏，返回dict，否则返回list'''
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('Sheet的类型不正确，请修正')
            elif type(self.sheet) == int:
                sheet = workbook.sheet_by_index(self.sheet)
            elif type(self.sheet) == str:
                sheet = workbook.sheet_by_name(self.sheet)

            if self.title:
                title = sheet.row_values(0)
                for col in range(1,sheet.nrows):
                    self._data.append(dict(zip(title,sheet.row_values(col))))

            else:
                for col in range(0,sheet.nrows):
                    self._data.append(sheet.row_values(col))
        return self._data