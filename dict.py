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

print("ID   Name    Gender  Age    Address     Course")
for student in st3_4_list:
    print(f"{student['id']}   {student['name']}    {student['gender']}  {student['age']}    {student['address']}     *")
