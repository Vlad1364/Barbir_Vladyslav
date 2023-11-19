################Task01##############
def ispalindrom(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        print("It's a palindrom")
    else:
        print("It's not a palindrom")

text = input("Введіть текст:")
ispalindrom(text)

text = input("Введіть текст:")
ispalindrom(text)
################Task02##############
text1 = input("Введіть перше слово:")
text2 = input("Введіть друге слово:")

text1 = list(text1.replace(" ", "").lower())
text2 = list(text2.replace(" ", "").lower())

if sorted(text1) == sorted(text2):
    print("Анаграми")
else:
    print("Не анаграми")
################Task03##############
date = input("Введіть дату народження у форматі YYYYMMDD:")

while True:
    sum = 0
    for simbol in date:
        sum += int(simbol)

    date = str(sum)

    if len(date) == 1:
        break

print(sum)
################Task04##############
def check_word_combination(word, combination):
    word_index = 0

    for char in combination:
        if char.lower() == word[word_index].lower():
            word_index += 1
            if word_index == len(word):
                return "Yes"

    return "No"
word_to_find = "dog"
combination1 = "vcxzxduybfdsobywuefgas"
combination2 = "vcxzxdcybfdstbywuefsas"

result1 = check_word_combination(word_to_find, combination1)
result2 = check_word_combination(word_to_find, combination2)

print(result1)  # Виведе "Yes"
print(result2)  # Виведе "No"
################Task05##############
while True:
    try:
        number = int(input(" Введіть ціле число: "))
        print(number/2)
        break
    except:
        print("Введене значення не є допустимим числом. Повторіть спробу...")
################Task06##############
def calculate_life_number(date):
    try:
        while True:
            total_sum = 0
            for char in date:
                total_sum += int(char)

            date = str(total_sum)

            if len(date) == 1:
                return total_sum
    except ValueError:
        print("Неправильний формат дати. Будь ласка, введіть дату у форматі YYYYMMDD.")
        return None
user_input = input("Введіть дату народження у форматі YYYYMMDD:")
result = calculate_life_number(user_input)

if result is not None:
    print("Число", result)
################Task07##############
def get_integer_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
        except ValueError:
            print("Error: wrong input. Please enter an integer.")

# Приклад використання
min_limit = 1
max_limit = 100
user_number = get_integer_input(f"Enter an integer between {min_limit} and {max_limit}: ", min_limit, max_limit)

print(f"You entered: {user_number}")
