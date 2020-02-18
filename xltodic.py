from pandas import *
xls = ExcelFile('2008.xlsx')
data = xls.parse(xls.sheet_names[0]).to_dict()
for i in data['Name']:
    print(data['Name'][i])
    print(data['Emails'][i])

