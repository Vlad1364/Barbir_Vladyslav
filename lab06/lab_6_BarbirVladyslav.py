################Task01##############
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
################Task02##############
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    days_per_month = {
        1: 31,
        2: 29 if is_year_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if 1 <= month <= 12:
        return days_per_month[month]
    else:
        return None
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
################Task03##############
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    days_per_month = {
        1: 31,
        2: 29 if is_year_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return days_per_month.get(month, None)

def day_of_year(year, month, day):
    if (1 <= month <= 12) and (1 <= day <= days_in_month(year, month)):
        day_count = day
        for m in range(1, month):
            day_count += days_in_month(year, m)
        return day_count
    else:
        return None
print(day_of_year(2000, 12, 31))
################Task04##############
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
################Task05##############
def liters_100km_to_miles_gallon(liters):
    miles_per_gallon = (100 * 3.785) / (liters * 1.609)
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    liters_per_100km = (100* 3.785) / (miles * 1.609)
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
################Task06##############
def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
print(is_a_triangle(3, 4, 5))
print(is_a_triangle(2, 3, 8))
################Task07##############
def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
    return False


print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(5, 12, 13))
print(is_a_right_triangle(3, 8, 10))
print(is_a_right_triangle(7, 8, 10))
