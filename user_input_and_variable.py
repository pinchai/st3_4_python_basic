from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["ID", "Name", "Gender", "Address"]
table.add_row(["STD0001", "srey neath", 'female', "Takeo"])

print(table)
