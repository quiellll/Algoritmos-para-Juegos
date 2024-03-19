def repeated(emp, bustedList):
    for identifier, rep in emp.items():
        if rep >= 3:
            bustedList.append(identifier)
    bustedList.sort()
    return bustedList


e = list(map(int, input().strip().split()))

employees = {}

for i in e:
    if i != -1:
        employees[i] = employees.get(i, 0) + 1

busted = []
busted = repeated(employees, busted)

for i in busted:
    print(i, end=" ")
