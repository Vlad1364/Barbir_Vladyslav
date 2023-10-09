################Task01##############

n = int(input("Введіть ціле число n: "))
result = n >= 100
print(result)


################Task02##############

x= int(input("Введіть значення x"))
y= int(input("Введіть значення y"))

if x>y:
    print(f"Найбільше значення це x:{x}")
else:
    print(f"Найбільше значення це y:{y}")

################Task03##############

user_input = input()

if user_input == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever")
elif user_input == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {user_input}!")

################Task04##############
income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
    if tax < 0:
        tax = 0
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = round(tax)
print("The tax is:", tax, "thalers")
################Task05##############
year = int(input("Enter a year: "))

if year >= 1582:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Common year")
else:
    print("Not within the Gregorian calendar period")
################Task06##############
secret_number = 777

while True:
    user_input = int(input("Введіть ціле число: "))
    if user_input != secret_number:
        print("Ха-ха! Ви застрягли у моїй петлі!")
    else:
        print(f"Молодець, магле! Тепер ти вільний. Секретне число було {secret_number}.")
        break
################Task07##############
import time

for i in range(1, 6):
    print("Міссісіпі", i)
    time.sleep(1)

print("Ready or not, here I come!")
################Task08##############
while True:
    user_input = input("Введіть слово: ")

    if user_input == "chupacabra":
        print("You've successfully left the loop.")
        break
################Task09##############
user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)
################Task10##############
user_word = input("Введіть слово: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)
################Task11##############
blocks_available = int(input("Введіть кількість доступних блоків: "))

height = 0

while blocks_available >= height + 1:
    height += 1
    blocks_available -= height

print("Максимальна висота піраміди:", height)
################Task12##############
c0 = int(input("Введіть натуральне число c0: "))
steps = 0
while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
print("Кількість кроків для досягнення мети:", steps)

