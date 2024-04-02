list_char = []
n = 5
for step in range(1, n+1):
    char_ = input("Enter character: ")
    list_char.append(char_)
uq_char = set(list_char)

result = []
for uq in uq_char:
    cout = 0
    for ch in list_char:
        if uq == ch:
            cout+=1
    result.append({
        'char': uq,
        'count': cout
    })

for res in result:
    print(res)


