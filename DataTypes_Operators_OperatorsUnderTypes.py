# 1. Write Python program to get the version(not inside interpreter).

import sys

print(sys.version)

# 2. Write Python program to display the current date and time.

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M")
print(f"Current Date and Time: {current_time}")


# 3. Write a Python program to create a new string which is n copies of a given string
# where n is a non-negative integer.


def create_string(string, n):
    return string * n


print(create_string('a', 10))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the parameter and area.


import math

user_input = int(input("Input the radius of the circle: "))
perimeter = 2 * user_input * math.pi
area = user_input ** 2 * math.pi
print(f"The perimeter is: {perimeter} \nThe area is {area}")


# 5. Write a Python program to check if a string starts with "if".


def check_string(string):
    return string.startswith('if')


print(check_string('Python'))

# 6. Write a Python program which accepts the user's first and last name and print them
# in reverse order with a space between them.

first_name = input("Input your first name: ")
last_name = input("Input your last name: ")
print(f"Hello {last_name} {first_name}")

# 7. Write a Python program to accept a filename from the user to print the extension of that. (With Regexp)

filename = input("Enter a filename")


# 8. Write a Python program to check three numbers and return true if one or more of them are small.
# A number is called "small" if it is in the range 1..10 inclusive.


def check_three_number(a, b, c):
    if 1 <= a <= 10 or 1 <= b <= 10 or 1 <= c <= 10:
        return True


print(check_three_number(50, 2, 8))


# 9. Write a Python program to check three numbers and return true if one or the other is small, but not both.
# A number is called "small" if it is in the range 1..10 inclusive.


def check_three_numbers(a, b, c):
    if (1 <= a <= 10 and b > 10 and c > 10) or \
            (a > 10 and b >= 1 and b <= 10 and c > 10) or \
            (a > 10 and b > 10 and c >= 1 and c <= 10):
        return True
    else:
        return False


print(check_three_numbers(22, 50, 1))

# 10. Write a Python program to print the following 'here document'.
string = "a string that you \"don't\" have to escape\nThis\nis a ....... multi-line\nheredoc string --------> example"

print(string)


# 11. Write a Python program to create a new string where "if" is added to the front of a given string.
# If the string already begins with "if", return the string unchanged.

def add_if(string):
    if string.startswith('if'):
        return 'Unchanged'
    else:
        return 'if' + string


add_if('ifstring')


# 12. Write a Python program to create a new string from a given string using the first three characters or whatever is
# there if the string is less than length 3. Return n copies of the string.

def create_string(string, n):
    if len(string) <= 3:
        return string * n
    return string[0:3] * n


print(create_string('abc', 3))

# 13. Write a Python program which accepts the radius of the sphere as input and compute the volume.

area_input = int(input('Enter area: '))
print(4 * math.pi * area_input ** 2)


# 14. Write a Python program to create a new string from a given string where the first and last characters have been exchanged.


def create_new_string(string):
    return string[-1] + string[1:-1] + string[0]


print(create_new_string("Python"))


# 15 Write a Python program to check two integers and return true if one of them is 20 otherwise return their sum.

def check_int(a, b):
    if a == 20 or b == 20:
        return 20
    return a + b


print(check_int(10, 22))


# 16 Write a Python program to find the greatest of three numbers.  

def find_greatest(a, b, c):
    if a > b and a > c:
        return f'a = {a} the greatest'
    elif b > a and b > c:
        return f'b = {b} the greatest'
    return f'c = {c} the greatest'


print(find_greatest(10, 22, 35))


# 17. Write a Python program to check if a number is within 10 of 100 or 200. (E.g. 90, 110, 190, 210)

def check(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    return False


print(check(190))


# 18. Write a Python program to compute the sum of the two integers,
# if the two values are equal return double their sum otherwise return their sum.

def compute(a, b):
    if a == b:
        return (a + b) * 2
    return a + b


print(compute(5, 4))

# 19. Write a Python program to print “Python Basic Exercises" 9 times.


for _ in range(9):
    print('Python Basic Exercises')


# 20. Write a Python program to create a new string from a given string with the last character added at the front and
# back of the given string. The length of the given string must be 1 or more.

def new_string(string):
    return string[-1] + string + string[-1]


# 21.Write a Python program to print 34 upto 41.

for i in range(34, 41 + 1):
    print(i)

# 22. Write a Python program to print even numbers from 1 to 10.

print("Even numbers between 2 to 10:")
for i in range(2, 11, 2):
    print(i)

# 23. Write a Python program to print odd numbers from 1 to 9.

print("Odd numbers between 1 to 9:")
for i in range(1, 10, 2):
    print(i)


# 24. Write a Python program to print the elements of a given array.

def print_arr(arr):
    for item in arr:
        print(item)


# 25. Write a Python program to check two non-negative integer values and return true if they have the same last digit.
def check_two_non_negative(a, b):
    if str(a)[-1] == str(b)[-1]:
        return True
    return False


print(check_two_non_negative(40, 40))

# 26. Write a Python program to retrieve the total marks where subject name and marks of a student stored in a hash.
subjects = {'Liberature': 74, 'Science': 89, 'Math': 91}
total = sum(subjects.values())

# 27. Write a Python program to print a specified character twenty times.

for _ in range(3):
    print('@' * 20)
    print('*' * 20)
    print('#' * 20)


# 28. Write a Python program to test whether a year is leap year or not.

def check_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is a leap year"
            else:
                return f"{year} is not a leap year"
        else:
            return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"


print(check_leap(2020))


# 29. Write a Python program to check whether a string 'Java' appears at index 1 in a given sting,
# if 'Java' appears return the string without 'Java' otherwise return the string unchanged.

def check_string(string):
    if 'java' in string[0:4].lower():
        return string[4:]
    return 'Unchanged'


# 30. Write a Python program to create a string using the first two characters (if present) of a given string
# if the first character is 'p' and second one is 's' otherwise return a blank string.

def create_string(string):
    if string[0].lower() == 'p' and string[1].lower() == 's':
        return 'ps'
    return ''


# 31. Write a Python program to check two integers and return whichever
# value is nearest to the value 10, or return 0 if two integers are equal.


def check(a, b):
    if a == b:
        return 0
    if abs(10 - a) < abs(10 - b):
        return a
    return b


# 32. Write a Python program to check two integer values and return true if they are both in the range 10..20 inclusive,
# or they are both in the range 20..30 inclusive.


def check(a, b):
    return (a in range(10, 21) and b in range(10, 21)) or (a in range(20, 31) and b in range(20, 31))


# 33. Write a Python program to check two positive integer values and return the larger value that is in the range 20..30
# inclusive, or return 0 if no number is in that range.


def check(a, b):
    if a in range(20, 31) and b in range(20, 31):
        if a > b:
            return a
        return b
    else:
        if a in range(20, 31) and b not in range(20, 31):
            return a
        elif a not in range(20, 31) and b not in range(20, 31):
            return 0
        return b


# 34. Write a Python program to count the number of 5's in a given array.

def count(list):
    total = 0
    for number in list:
        if number == 5:
            total += 1

    return total


# 35. Write a Python program to check two non-negative integer values and return true if they have the same last digit.
def check_two_non_negative(a, b):
    if str(a)[-1] == str(b)[-1]:
        return True
    return False


# 36. Write a Python program to check if the sequence of numbers 10, 20, 30
# appears anywhere in a given array of integers.

def check_sequence(array):
    index = array.index(10)
    if array[index:index + 3] == [10, 20, 30]:
        return True
    return False


# 37. Write a Python program to check two given integers and return 11 if either one is 11.
# Return their sum or difference if sum or difference is 11.

def check(a, b):
    if a or b == 1:
        return 11
    else:
        if a + b == 11:
            return a + b
        elif abs(a - b) == 11:
            return a - b
    return 0


# 38. Write a Python program to check three given integers and return true if one of them is 20
# or more less than one of the others.

def check(a, b, c):
    return abs(a - b) >= 20 or abs(b - c) >= 20 or abs(c - a) >= 20


# 39 Write a Python program to check two given integers and return the larger value.
# However, if the two values have the same remainder when divided by 5 then return the smaller value and if the two values are the same, return 0.

def check(a, b):
    if a == b:
        return 0
    elif a % 5 == b % 5:
        if a < b:
            return a
        return b
    elif a > b:
        return a
    return b


# 40. Write a Python program to check two given integers, each in the range 10..99,
# return true if there is a digit that appears in both numbers.

def check(a, b):
    a = list(str(a))
    b = list(str(b))
    for number in a:
        if number in b:
            return True
    for number in b:
        if number in a:
            return True
    return False


# 41. Write a Python program to check three given integers x, y, z and return true if one of y or z is close
# (differing from a by at most 1), while the other is far, differing from both other values by 3 or more

def check(x, y, z):
    return abs(x - y) == 1 and (abs(x - z) and abs(y - z)) >= 3


#42. На зустріч один одному відповідно з міста А та міста Б рухається заєць та черепаха.
# Ввести з клавіатури відстань між містами, швидкість зайця та швидкість черепахи.
# Обчислити на якій відстані від міста Б вони зустрінуться.

distance_between_cities = int(input("Enter distance between cities: "))
turtle_speed = int(input("Enter turtle speed: "))
bunny_speed = int(input("Enter bunny speed: "))
print((distance_between_cities/(turtle_speed+bunny_speed)) * turtle_speed)


#44.Написати програму, яка визначає дату наступного дня, на основі сьогоднішньої дати.

from datetime import datetime, timedelta
current_day = datetime.now()
one_day = timedelta(1)
print(current_day + one_day)


#45. Написати программу, яка задає категорію та стаж працівника, а також ставку відповідно до категорії(1-ша категорія—3000, 2-га – 2000, 3-тя -- 1000).
# Обчислити заробітну плату, враховуючи надбавку за стаж роботи(до 2 років—0%, від 2 до 5 – 10%, від 5 до 10 – 20%, більше 10—30% ) і зняття податку – 15%.
categories = {1: 3000, 2: 2000, 3: 1000}

def calculate_salary(category, experience):
    salary = categories[category]
    bonus = 0
    if experience in range(2):
        bonus = 0
    elif experience in range(2,5):
        bonus = 10
    elif experience in range(5, 10):
        bonus = 20
    if experience >= 10:
        bonus = 30

    bonus = (salary * bonus)/100
    salary += bonus
    commission = (salary * 15)/100
    salary -= commission
    print(salary)


#46. Написати програму, яка із введеного користувачем цілого чотирьохзначного числа (наприклад 5141):
#знаходить суму цифр цього числа (5141 це 5+1+4+1 = 11).
#перевіряє чи є однакові цифри (двічі зустрічається цифра 1)
#перевіряє чи сума двох перших цифр чотирьохзначного числа рівна двом наступним (5141 → 5+1 = 6 і 4+1 = 5 → суми першої та другої пар цифр даного числа різні)

def check(numbers):
    numbers = [int(number) for number in str(numbers)]
    total = 0
    for number in numbers:
        total += number
    print("Total sum of {0} = {1}".format("".join(map(str, numbers)), total))
    set_numbers = set(numbers)
    if len(set_numbers) != len(numbers):
        print("Contains duplicates")
    if sum(numbers[:2]) == sum(numbers[2:]):
        print(f"Sum of first pair {numbers[:2]} equals Sum of second pair {numbers[2:]}")
    else:
        print(f"Sum of first pair {numbers[:2]} doesn't equals Sum of second pair {numbers[2:]}")


# 47. Написати програму, яка обчислює, скільки повинен заплатити водій за паркування автомобіля на стоянці протягом певного часу.
# Користувач вводить наступні дані: час заїзду на стоянку (у годинах і хвилинах), час від’їзду, вартість однієї години паркування.
# Водій платить за кожну повну годину. Також, здійснюється плата за перевищення користування стоянкою більше ніж на 10 хв., наприклад:
# якщо хтось використав стоянку протягом 2 год. і 15 хв., то повинен заплатити за 3 год. В кінцевому результаті на екран необхідно вивести повідомлення про час
# заїзду та виїзду авто, ціну за годину паркування і повну вартість.

def parking_calulate(arrival_time, departure_time, price):
    arrival = [int(time) for time in arrival_time.split(':')]
    departure = [int(time) for time in departure_time.split(':')]
    total_price = (departure[0] - arrival[0]) * price
    if (departure[1] - arrival[1]) >= 10:
        total_price += price
    print("You arrive at {0} - your departure time - {1}. Total price: {2}".format(arrival_time, departure_time, total_price))


