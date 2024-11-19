first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))
second_result = (len(first[i]) - len(second[i]) for i in range(len(first)) if i < len(second))

print("first_result:", list(first_result))  # Преобразуем генератор в список для вывода
print("second_result:", list(second_result))  # Преобразуем генератор в список для вывода