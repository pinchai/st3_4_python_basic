from prettytable import PrettyTable
import random

table = PrettyTable()

st3_4_list = [
    {
        'id': '001',
        'name': 'buntek',
        'gender': 'male',
        'age': 21,
        'address': 'PhnomPenh',
        'course': ['c++', 'c#', 'java', 'php']
    },
    {
        'id': '002',
        'name': 'cheu',
        'gender': 'male',
        'age': 22,
        'address': 'Speu',
        'course': ['c++', 'c#', 'java', 'php']
    }
]

table.field_names = [
    "ID",
    "Name",
    "Gender",
    "Age",
    "Address",
    "Course"
]
for student in st3_4_list:
    table.add_row([
        student['id'],
        student['name'],
        student['gender'],
        student['age'],
        student['address'],
        '*'])
print(table)
