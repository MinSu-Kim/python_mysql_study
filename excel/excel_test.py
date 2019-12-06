import pandas as pd

df = pd.read_excel('excel_file.xlsx')
print(df)

excel_examl_data1 = {'학생':['A', 'B', 'C', 'D', 'E', 'F'],
                     '국어':[80, 90, 95, 70, 75, 85],
                     '영어':[90, 95, 70, 85, 90, 95],
                     '수학':[85, 95, 75, 80, 85, 100]}
df1 = pd.DataFrame(excel_examl_data1, columns=['학생', '국어', '영어', '수학'])
print(df1)

excel_writer = pd.ExcelWriter('excel_output.xlsx', engine='xlsxwriter')
df1.to_excel(excel_writer, index=False)
excel_writer.save()