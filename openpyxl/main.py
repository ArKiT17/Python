import openpyxl
from openpyxl.chart import (
    Reference,
    Series,
    BarChart
)

NUMBER_OF_STUDENTS = 12

b = openpyxl.load_workbook("list.xlsx")
s = b.active

rows = s['B2:D13']
val2 = []
index = 0
for row in rows:
    onerow = []
    for i in row:
        onerow.append(i.value)
    val2.append(sum(onerow))
for i in range(0, NUMBER_OF_STUDENTS):
    s.cell(row=i+2, column=5).value = val2[i]

tmp = []
for j in range(2, 5):
    coll = []
    for i in range(2, 2+NUMBER_OF_STUDENTS):
        coll.append(s.cell(row=i, column=j).value)
    tmp.append(sum(coll))
for i in range(0, 3):
    s.cell(row=2+NUMBER_OF_STUDENTS, column=2+i).value = tmp[i]

s.auto_filter.ref = 'E1:E13'
s.auto_filter.add_sort_condition('E1:E13')
# for i in range(int(NUBER_OF_STUDENTS*0.45)):
#     s.cell(row=2+i, column=6).value = "Нараховано стипендію"
s.cell(row=2+NUMBER_OF_STUDENTS, column=6).value = "Нараховано стипендію першим {} студентам".format(int(NUMBER_OF_STUDENTS*0.45))

data = Reference(s, min_col=5, min_row=2, max_row=2+NUMBER_OF_STUDENTS)
categs = Reference(s, min_col=1, min_row=2, max_row=2+NUMBER_OF_STUDENTS)

chart = BarChart()
chart.add_data(data=data)
chart.set_categories(categs)

chart.legend = None
chart.y_axis.majorGridlines = None
chart.varyColors = True
chart.title = "Сума балів з усіх дисциплін"

s.add_chart(chart, "A16")

b.save("list2.xlsx")