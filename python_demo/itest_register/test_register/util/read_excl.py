import xlrd
from xlutils.copy import copy
class ReadExcle():
    def __init__(self,excle_path = None,index = None ):#excle_path表格的路径，index表格的页数
        if excle_path == None:
            self.excle_path = 'E:/python_demo/potest/register_data.xls'
        else:
            self.excle_path = excle_path
        if index == None:
            index = 0
        #获取表格数据
        self.data = xlrd.open_workbook(self.excle_path)
        self.table = self.data.sheets()[index]
    #获取表格每行数据，添加到一个大的list
    def get_excle_data(self):
        result = []
        #获取表格行数
        rows = self.get_lines()
        #判断行数是否不为空
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                print(col)
                result.append(col)
            return result
        return None
    #获取行数
    def get_lines(self):
        #获取表格行数
        rows = self.table.nrows
        #判断行数是否大于1
        if rows >= 1:
            return rows
        return None
    #获取单元格数据
    def get_col_value(self,row,col):
        #获取表格行数
        rows = self.get_lines()
        if rows > row:
            data = self.table.cell(row,col).value
            return data
        return None
    #写入数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.excle_path)
        write_data = copy(read_data)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save(self.excle_path)
if __name__ == '__main__':
    ex = ReadExcle()
    print(ex.get_col_value(2,2))
    print(ex.write_value(8,2,'test'))