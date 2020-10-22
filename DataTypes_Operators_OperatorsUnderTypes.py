# 1. Write Python program to get the version(not inside interpreter).

import sys


def return_version():
    return sys.version


print(return_version())

# 2. Write Python program to display the current date and time.

from datetime import datetime


def display_current_date():
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M")
    return current_time


print(display_current_date())


# 3. Write a Python program to create a new string which is n copies of a given string
# where n is a non-negative integer.


def create_string(string, n):
    return string * n


print(create_string('a', 10))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the parameter and area.


import math


def calculate_area_and_perimeter():
    user_input = int(input("Input the radius of the circle: "))
    perimeter = 2 * user_input * math.pi
    area = user_input ** 2 * math.pi
    return perimeter, area


print(calculate_area_and_perimeter())


# 5. Write a Python program to check if a string starts with "if".


def check_string(string):
    return string.startswith('if')


print(check_string('Python'))


# 6. Write a Python program which accepts the user's first and last name and print them
# in reverse order with a space between them.

def print_in_reverse():
    first_name = input("Input your first name: ")
    last_name = input("Input your last name: ")
    return f"Hello {last_name} {first_name}"


print(print_in_reverse())
# 7. Write a Python program to accept a filename from the user to print the extension of that. (With Regexp)
import re


def show_extension():
    filename = input('Enter a filename: ')
    pattern = r'\W'
    result = re.split(pattern, filename)
    return result[0], result[1]


print(show_extension())


# 8. Write a Python program to check three numbers and return true if one or more of them are small.
# A number is called "small" if it is in the range 1..10 inclusive.

def check_in_range_of_10(number):
    return 1 <= number <= 10


def check_three_number(a, b, c):
    return check_in_range_of_10(a) or check_in_range_of_10(b) or check_in_range_of_10(c)


print(check_three_number(50, 2, 8))


# 9. Write a Python program to check three numbers and return true if one or the other is small, but not both.
# A number is called "small" if it is in the range 1..10 inclusive.

def number_is_small(number):
    range_of_ten = range(1, 11)
    return number in range_of_ten


def check_three_numbers(a, b, c):
    a_is_small = number_is_small(a) and not number_is_small(b) and not number_is_small(c)
    b_is_small = number_is_small(b) and not number_is_small(a) and not number_is_small(c)
    c_is_small = number_is_small(c) and not number_is_small(b) and not number_is_small(b)
    return a_is_small or b_is_small or c_is_small


print(check_three_numbers(22, 50, 1))


# 10. Write a Python program to print the following 'here document'.
def print_document():
    string = "a string that you \"don't\" have to escape\nThis\nis a ....... multi-line\nheredoc string --------> " \
             "example "
    return string


print(print_document())


# 11. Write a Python program to create a new string where "if" is added to the front of a given string.
# If the string already begins with "if", return the string unchanged.

def add_if(string):
    if string.startswith('if'):
        return 'Unchanged'
    else:
        return 'if' + string


print(add_if('ifstring'))


# 12. Write a Python program to create a new string from a given string using the first three characters or whatever is
# there if the string is less than length 3. Return n copies of the string.

def create_string(string, n):
    if len(string) <= 3:
        return string * n
    return string[0:3] * n


print(create_string('abc', 3))


# 13. Write a Python program which accepts the radius of the sphere as input and compute the volume.
def compute_the_volume(number):
    return 4 * math.pi * number ** 2


print(compute_the_volume(20))


# 14. Write a Python program to create a new string from a given string where the first and last characters have been
# exchanged.


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

def print_n_times(n):
    for _ in range(n):
        print('Python Basic Exercises')


print_n_times(9)


# 20. Write a Python program to create a new string from a given string with the last character added at the front and
# back of the given string. The length of the given string must be 1 or more.

def new_string(string):
    return string[-1] + string + string[-1]


print(new_string('Python'))


# 21.Write a Python program to print 34 upto 41.

def print_in_range(start, end):
    for i in range(start, end + 1):
        print(i)


print_in_range(34, 41)


# 22. Write a Python program to print even numbers from 1 to 10.

def print_even_numbers(end):
    print(f"Even numbers between {1} to {end}:")
    for i in range(2, end + 1, 2):
        print(i)


print_even_numbers(10)


# 23. Write a Python program to print odd numbers from 1 to 9.

def print_odd_numbers(end):
    print(f"Even numbers between {1} to {end}:")
    for i in range(1, end + 1, 2):
        print(i)


print_odd_numbers(10)


# 24. Write a Python program to print the elements of a given array.

def print_list(number):
    for item in number:
        print(item)


print_list([1, 2, 3, 4, 5])


# 25. Write a Python program to check two non-negative integer values and return true if they have the same last digit.
def check_two_non_negative(a, b):
    if str(a)[-1] == str(b)[-1]:
        return True
    return False


print(check_two_non_negative(40, 40))


def check_two_non_negative_v2(number1, number2):
    number1 = [int(number) for number in str(number1)]
    number2 = [int(number) for number in str(number2)]
    if list(number1)[-1] == list(number2)[-1]:
        return True
    return False


print(check_two_non_negative_v2(40, 40))


def check_two_non_negative_v3(number1, number2):
    return number1 % 10 == number2 % 10


print(check_two_non_negative_v3(43, 3))


# 26. Write a Python program to retrieve the total marks where subject name and marks of a student stored in a hash.

def count_sum_of_marks(subjects):
    return sum(subjects.values())


print(count_sum_of_marks({'Literature': 74, 'Science': 89, 'Math': 91}))


# 27. Write a Python program to print a specified character twenty times.

def print_twenty_times(string):
    return string * 20


print(print_twenty_times('@'))


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


print(check_string('Java'))


# 30. Write a Python program to create a string using the first two characters (if present) of a given string
# if the first character is 'p' and second one is 's' otherwise return a blank string.

def create_string(string):
    if string[0].lower() == 'p' and string[1].lower() == 's':
        return 'ps'
    return ''


print(create_string('ps'))


# 31. Write a Python program to check two integers and return whichever
# value is nearest to the value 10, or return 0 if two integers are equal.


def check(a, b):
    if a == b:
        return 0
    if abs(10 - a) < abs(10 - b):
        return a
    return b


print(check(5, 19))


# 32. Write a Python program to check two integer values and return true if they are both in the range 10..20 inclusive,
# or they are both in the range 20..30 inclusive.


def check_if_values_in_range(num1, num2):
    range_between_ten_and_twenty = range(10, 21)
    range_between_twenty_and_thirty = range(20, 31)

    return num1 in range_between_ten_and_twenty and num2 in range_between_ten_and_twenty or \
           num1 in range_between_twenty_and_thirty and num2 in range_between_twenty_and_thirty


print(check_if_values_in_range(10, 15))


# 33. Write a Python program to check two positive integer values and return the larger value that is in the range
# 20..30 inclusive, or return 0 if no number is in that range.


def check_if_values_in_range(num1, num2):
    range_between_twenty_and_thirty = range(20, 31)
    if num1 in range_between_twenty_and_thirty and num2 in range_between_twenty_and_thirty:
        if num1 > num2:
            return num1
        return num2
    else:
        if num1 in range_between_twenty_and_thirty and num2 not in range_between_twenty_and_thirty:
            return num1
        elif num1 not in range_between_twenty_and_thirty and num2 not in range_between_twenty_and_thirty:
            return 0
        return num2


print(check_if_values_in_range(40, 40))


# 34. Write a Python program to count the number of 5's in a given array.

def count_times_number_appears(numbers, value=5):
    total = 0
    for number in numbers:
        if number == value:
            total += 1
    return total


print(count_times_number_appears([1, 2, 3, 4, 5, 5, 5]))


def count_times_number_appears_v2(numbers, value=5):
    return len([number for number in numbers if number == value])


print(count_times_number_appears_v2([1, 2, 5, 5, 5, 5, 5, 2, 3]))


# 35. Write a Python program to check two non-negative integer values and return true if they have the same last digit.
def check_two_non_negative(a, b):
    if str(a)[-1] == str(b)[-1]:
        return True
    return False


print(check_two_non_negative(40, 40))


def check_two_non_negative_v2(number1, number2):
    number1 = [int(number) for number in str(number1)]
    number2 = [int(number) for number in str(number2)]
    if list(number1)[-1] == list(number2)[-1]:
        return True
    return False


print(check_two_non_negative_v2(40, 40))


# 36. Write a Python program to check if the sequence of numbers 10, 20, 30
# appears anywhere in a given array of integers.

def check_if_sequence_in_numbers(numbers):
    index = numbers.index(10)
    if numbers[index:index + 3] == [10, 20, 30]:
        return True
    return False


print(check_if_sequence_in_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]))


# 37. Write a Python program to check two given integers and return 11 if either one is 11.
# Return their sum or difference if sum or difference is 11.

def check_for_eleven(num1, num2):
    if num1 or num2 == 11:
        return 11
    else:
        if num1 + num2 == 11:
            return num1 + num2
        elif abs(num1 - num2) == 11:
            return num1 - num2
    return 0


print(check_for_eleven(6, 5))


# 38. Write a Python program to check three given integers and return true if one of them is 20
# or more less than one of the others.

def check(num1, num2, num3):
    return abs(num1 - num2) >= 20 or abs(num2 - num3) >= 20 or abs(num3 - num1) >= 20


print(check(20, 50, 100))


# 39 Write a Python program to check two given integers and return the larger value. However, if the two values have
# the same remainder when divided by 5 then return the smaller value and if the two values are the same, return 0.

def check_larger_value(num1, num2):
    if num1 == num2:
        return 0
    elif num1 % 5 == num2 % 5:
        if num1 < num2:
            return num1
        return num2
    elif num1 > num2:
        return num2
    return num1


print(check_larger_value(10, 50))


# 40. Write a Python program to check two given integers, each in the range 10..99,
# return true if there is a digit that appears in both numbers.

def containts_same_digit(num1, num2):
    num1 = [int(number) for number in str(num1)]
    num2 = [int(number) for number in str(num2)]
    for number in num1:
        if number in num2:
            return True
    return False


print(check(50, 10))


# 41. Write a Python program to check three given integers x, y, z and return true if one of y or z is close
# (differing from a by at most 1), while the other is far, differing from both other values by 3 or more

def check(x, y, z):
    return abs(x - y) == 1 and (abs(x - z) and abs(y - z)) >= 3


print(check(5, 4, 10))


# 42. На зустріч один одному відповідно з міста А та міста Б рухається заєць та черепаха.
# Ввести з клавіатури відстань між містами, швидкість зайця та швидкість черепахи.
# Обчислити на якій відстані від міста Б вони зустрінуться.

def calculate_distance():
    distance_between_cities = int(input('Enter distance between cities: '))
    turtle_speed = int(input('Enter turtle speed: '))
    bunny_speed = int(input('Enter bunny speed: '))
    result = distance_between_cities / (turtle_speed + bunny_speed) * turtle_speed
    return result


calculate_distance()

# 44.Написати програму, яка визначає дату наступного дня, на основі сьогоднішньої дати.

from datetime import datetime, timedelta


def determine_next_day():
    current_day = datetime.now()
    one_day = timedelta(1)
    return current_day + one_day


print(determine_next_day())

# 45. Написати программу, яка задає категорію та стаж працівника, а також ставку відповідно до категорії(1-ша
# категорія—3000, 2-га – 2000, 3-тя -- 1000). Обчислити заробітну плату, враховуючи надбавку за стаж роботи(до 2
# років—0%, від 2 до 5 – 10%, від 5 до 10 – 20%, більше 10—30% ) і зняття податку – 15%.
categories = {1: 3000, 2: 2000, 3: 1000}


def calculate_salary(category, experience):
    salary = categories[category]
    bonus = 0
    if experience in range(2):
        bonus = 0
    elif experience in range(2, 5):
        bonus = 10
    elif experience in range(5, 10):
        bonus = 20
    if experience >= 10:
        bonus = 30

    bonus = (salary * bonus) / 100.0
    salary += bonus
    commission = (salary * 15) / 100.0
    salary -= commission
    return salary


print(calculate_salary(2, 4))


# 46. Написати програму, яка із введеного користувачем цілого чотирьохзначного числа (наприклад 5141): знаходить суму
# цифр цього числа (5141 це 5+1+4+1 = 11). перевіряє чи є однакові цифри (двічі зустрічається цифра 1) перевіряє чи
# сума двох перших цифр чотирьохзначного числа рівна двом наступним (5141 → 5+1 = 6 і 4+1 = 5 → суми першої та другої
# пар цифр даного числа різні)

def check(numbers):
    numbers = [int(number) for number in str(numbers)]
    total = 0
    for number in numbers:
        total += number
    print("Total sum of {0} = {1}".format("".join(map(str, numbers)), total))
    if len(set(numbers)) != len(numbers):
        print("Contains duplicates")
    if sum(numbers[:2]) == sum(numbers[2:]):
        print(f"Sum of first pair {numbers[:2]} equals Sum of second pair {numbers[2:]}")
    else:
        print(f"Sum of first pair {numbers[:2]} doesn't equals Sum of second pair {numbers[2:]}")


check(5141)


# 47. Написати програму, яка обчислює, скільки повинен заплатити водій за паркування автомобіля на стоянці протягом
# певного часу. Користувач вводить наступні дані: час заїзду на стоянку (у годинах і хвилинах), час від’їзду,
# вартість однієї години паркування. Водій платить за кожну повну годину. Також, здійснюється плата за перевищення
# користування стоянкою більше ніж на 10 хв., наприклад: якщо хтось використав стоянку протягом 2 год. і 15 хв.,
# то повинен заплатити за 3 год. В кінцевому результаті на екран необхідно вивести повідомлення про час заїзду та
# виїзду авто, ціну за годину паркування і повну вартість.

def calculate_parking(arrival_time, departure_time, price):
    arrival = [int(time) for time in arrival_time.split(':')]
    departure = [int(time) for time in departure_time.split(':')]
    total_price = (departure[0] - arrival[0]) * price
    if departure[1] - arrival[1] >= 10:
        total_price += price
    print("You arrive at {0} - your departure time - {1}. Total price: {2}".format(arrival_time, departure_time,
                                                                                   total_price))
    return total_price


print(calculate_parking('15:20', '16:25', 10))
