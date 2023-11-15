################Task01##############
n = int(input("Введіть число n: "))
numbers = tuple(map(int, input("Введіть числа через пробіл: ").split()))
result = [num for num in numbers if num < n]
print("Числа, менші за", n, ":", result)
################Task02##############
strings_tuple = ("Влад", "Дмитро", "Іван")
result_string = ', '.join(strings_tuple)
print("Результат з'єднання рядків:", result_string)
################Task03##############
ukrainian_library = {
    "Кобзар": {"Автор": "Тарас Шевченко", "Рік видання": 1840, "Кількість сторінок": 200},
    "Захар Беркут": {"Автор": "Іван Франко", "Рік видання": 1891, "Кількість сторінок": 300},
    "Лісова пісня": {"Автор": "Леся Українка", "Рік видання": 1911, "Кількість сторінок": 250},
}
book_title = input("Введіть назву книги: ")
if book_title in ukrainian_library:
    book_info = ukrainian_library[book_title]
    print(f"\nІнформація про книгу '{book_title}':")
    print(f"Автор: {book_info['Автор']}")
    print(f"Рік видання: {book_info['Рік видання']}")
    print(f"Кількість сторінок: {book_info['Кількість сторінок']}")
else:
    print(f"\nКнига '{book_title}' не знайдена в бібліотеці.")
################Task04##############
# Створення словника із інформацією про студентів
students_info = {
    "Литвиненко": {"ПІБ": "Литвиненко Владислав Іванович", "Вік": 22, "Спеціальність": "КР-121", "Заліковка": "32123456"},
    "Олійник": {"ПІБ": "Олійник Оксана Вікторівна", "Вік": 20, "Спеціальність": "КІ-120", "Заліковка": "12789012"},
    "Федоров": {"ПІБ": "Федоров Дмитро Сидорович", "Вік": 21, "Спеціальність": "КМ-134", "Заліковка": "65345678"},
}
student_lastname = input("Введіть прізвище студента: ")
if student_lastname in students_info:
    student_info = students_info[student_lastname]
    print("\nІнформація про студента:")
    print(f"ПІБ: {student_info['ПІБ']}")
    print(f"Вік: {student_info['Вік']}")
    print(f"Спеціальність: {student_info['Спеціальність']}")
    print(f"Заліковка: {student_info['Заліковка']}")
else:
    print(f"\nСтудента із прізвищем '{student_lastname}' не знайдено.")
################Task05##############
contacts = {
    "Владислав": ["+380991234567", "+380991112233"],
    "Андрій": ["+380991234555", "+380991234666"],
    "Ірина": ["+380991234777"],
}
def add_number(name, new_number):
    if name in contacts:
        contacts[name].append(new_number)
        print(f"New number {new_number} added for contact {name}")
    else:
        print(f"Contact with the name {name} not found in the phone book.")

add_number("Андрій", "+380991234888")

print("\nList of phone numbers for all contacts:")
for name, numbers in contacts.items():
    print(f"{name}: {', '.join(numbers)}")