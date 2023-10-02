#################Task1################
import math
μ = float(input("Введіть значення μ: "))
σ = float(input("Введіть значення σ: "))
x = float(input("Введіть значення x: "))

y = 1 / (σ * math.sqrt(2 * math.pi)) * math.exp(-((x - μ) ** 2) / (2 * σ ** 2))

print(f'Значення функції Гауса для x = {x}, μ = {μ}, σ = {σ}: {y}')

#################Task2################
john = 3
mary = 5
adam = 6
print(f'john: {john}, mary: {mary}, adam: {adam}')
totalApple = john + mary + adam
print(totalApple)
print(f"Загальна кількість яблук: {totalApple}")

#################Task3################
miles = 7.38
kilometers = 12.25

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#################Task4################
x = 1
x = float(x)
y = 3 * (x**3) - 2 * (x**2) + 3**x - 1
print("y =", y)

#################Task5################

# this program computes the number of seconds in a given number of hours

hours = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Seconds in Hours: ", hours * seconds) # printing the number of seconds in a given number of hours

#this is the end of the program that computes the number of seconds in 2 hour

#################Task6################

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

print("Додавання:",a+b)
print("Віднімання:",a-b)
print("Множення:",a*b)
if b != 0:
    print("Ділення:", a / b)
else:
    print("Помилка: Ділення на нуль неможливе.")

#################Task7################

x = float(input("Enter value for x: "))

y= 1 / (x + (1 / (x + (1 / (x + (1 / (x + (1 / x))))))))

print("y =", y)

#################Task8################

start_hour = int(input("Введіть години початку (0-23): "))
start_minute = int(input("Введіть хвилини початку (0-59): "))
duration_minutes = int(input("Введіть тривалість події у хвилинах: "))
end_hour = (start_hour + (start_minute + duration_minutes) // 60) % 24
end_minute = (start_minute + duration_minutes) % 60

print(f"Подія закінчується о {end_hour}:{end_minute}")