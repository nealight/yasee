import pandas

"""
ser = pandas.Series(["soo", 200], ["Nancy", "Boo"])
ser = ser * 2
print(ser.__str__().split())


d = {"one": pandas.Series([100., 200.], ["apple", "ball"]),
     "two": pandas.Series([200., 400.], ["apple", "ball"])}

df = pandas.DataFrame(d)
print(df)

"""

intermediate = pandas.ExcelFile("../reports/report.xlsx")
file = intermediate.parse(intermediate.sheet_names[0])

row_0 = file.iloc[0]
print(str(row_0))
