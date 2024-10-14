first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (False if len(first[i]) != len(second[i]) else True for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))

