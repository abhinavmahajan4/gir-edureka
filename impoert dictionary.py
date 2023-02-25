from pandas import *
xls = ExcelFile('converted.xls')
df = xls.parse()
print (df.to_dict())