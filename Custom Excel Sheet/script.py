from collections import OrderedDict
import xlsxwriter


data = {"1":["xyz",""],"2":["abc","def"],"3":["zzz",""]}

# Use an OrderedDict to maintain the order of the columns
data = OrderedDict((k,data.get(k)) for k in sorted(data.keys()))

# Open an Excel workbook
workbook = xlsxwriter.Workbook('dict_to_excel.xlsx')

# Set up a format
book_format = workbook.add_format(properties={'bold': True, 'font_color': 'red'})

# Create a sheet
worksheet = workbook.add_worksheet('dict_data')

# Write the headers
for col_num, header in enumerate(data.keys()):
    worksheet.write(0,col_num, int(header))

# Save the data from the OrderedDict into the excel sheet
for row_num,row_data in enumerate(zip(*data.values())):
    for col_num, cell_data in enumerate(row_data):
        if cell_data ==  "xyz":
            worksheet.write(row_num+1, col_num, cell_data, book_format)
        else:
            worksheet.write(row_num+1, col_num, cell_data)

# Close the workbook
workbook.close()