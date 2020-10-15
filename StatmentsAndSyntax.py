# 1. Write a Python program to check if a value exists in an array.

def check_value(value, numbers):
    print(f'Check if \'{value}\' in array!')
    return value in numbers


# 2. Write a Python program to check whether 7 appears as either the first or last element in a given array.
# The array length must be 1 or more.


def check_number(numbers):
    if numbers:
        return numbers[0] == 7 and numbers[-1] == 7


# 3. Write a Python program to pick a number of random elements from a given array.
import random


def two_random(numbers, number_of_elements):
    print(f'Original array:\n{numbers}')
    print(f'{number_of_elements} random elements from the array.')
    random.shuffle(numbers)
    return numbers[:number_of_elements]


# 4. Write a Python program to check whether first and the last element are the same as a given array of integers.
# The array length must be 1 or more.

def check_first_and_last(numbers):
    if numbers:
        return numbers[0] == numbers[-1]


# 5. Write a Python program to compute the sum of elements in a given array.

def sum_of_elements(numbers):
    print(f'Original array:\n{numbers}')
    print('Sum of the values of the above array:')
    return sum(numbers)


# 6. Write a Python program to remove duplicate elements from a given array.

def remove_duplicate(numbers):
    print(f'Original array: {numbers}')
    print('Array with unique elements:')
    return set(numbers)


# 7. Write a Python program to check two given arrays of integers and test if they have the same first element
# or they have the same last element. Both arrays length must be 1 or more.

def check_same(numbers1, numbers2):
    if numbers1 and numbers2:
        return numbers1[0] == numbers2[0] or numbers1[-1] == numbers2[-1]


# 8. Write a Python program to remove blank elements from a given array.


def remove_blank_elements(elements):
    print(f'Original array: {elements}')
    print('Remove a blank element from above array:')
    return list(filter(lambda x: x, elements))


# 9. Write a Python program to split a delimited string into an array.

def split_string(string):
    strings = []
    numbers = []
    for item in string.split(', '):
        if item.isdigit():
            numbers.append(int(item))
        else:
            strings.append(item)
    if strings: print(strings)
    if numbers: print(numbers)


# 10. Write a Python program to create an array with the elements "rotated left" of a given array of ints length 3.

def rotated_left(numbers):
    return numbers[1:] + numbers[:1]


# 11. Write a Python program to create a new array with the elements in reverse order
# from a given an array of integers length 3.

def reverse_order(numbers):
    return numbers[::-1]


# 12. Write a Python program to find the larger between the first and last elements of a given array of integers
# and length 3. Replace all the other values to be that value. Return the changed array.


def find_larger(numbers):
    if numbers[0] > numbers[-1]:
        max_number = numbers[0]
    else:
        max_number = numbers[-1]
    return [max_number for _ in numbers]


# 13. Write a Python program to concatenate an array of arrays into one.

def concat(numbers1, numbers2):
    return numbers1 + numbers2


# 14. Write a Python program to check if a given array of integers contains 3 twice, or 5 twice.


def check_integers(numbers):
    return numbers.count(3) == 2 or numbers.count(5) == 2



# 15. Write a Python program to find the largest odd value from a given array

def find_largest(numbers):
    return max([number for number in numbers if number % 2 != 0])


# 16. Write a Python program to create a new array using the first three elements of a given array of integers.

def create_array(numbers):
    return numbers[:3]


# 17. Write a Python program to get the number of even integers in a given array.

def sum_of_even(numbers):
    return len([number for number in numbers if number % 2 == 0])


# 18. Write a Python program to find the difference between the largest and smallest values of a given array of
# integers.

def difference_between_maxmin(numbers):
    return max(numbers) - min(numbers)


# 19. Write a Python program to compute the average values of a given array of except the largest and smallest values.

def compute_avg(numbers):
    numbers.sort()
    return sum(numbers[1:-1]) / len(numbers[1:-1])


# 20. Write a Python program to compute the sum of the numbers of a given array except for the number 17 and numbers
# that come immediately after a 17.

def compute_sum(numbers):
    return sum([number for number in numbers if number < 17])


# 21. Write a Python program to compute the sum of every third element of a given array of integers.
def compute_sum_of_every_third(numbers):
    return sum(numbers[2::3])


# 22. Write a Python program to check whether every element is a 3 or a 5 in a given array of integers.

def check_element(numbers):
    return numbers.count(3) == len(numbers) or numbers.count(5) == len(numbers)


# 23. Write a Python program to check whether a given value appears everywhere in a given array.
# A value is "everywhere" in an array if it presents for every pair of adjacent elements in the array.

def check_if_appears(numbers, number):
    for i in range(len(numbers)):
        if number not in numbers[i:i + 2]:
            return False
    return True


# 24. Write a Python program to check whether a given array contains a 3 next to a 3 or a 5 next to a 5, but not both.

def contains_numbers(numbers, num1=3, num2=5):
    is_next_three, is_next_five = None, None
    if num1 in numbers:
        num1_index = numbers.index(num1)
        is_next_three = num1 == numbers[num1_index + 1]
    if num2 in numbers:
        num2_index = numbers.index(num2)
        is_next_five = num2 == numbers[num2_index + 1]

    if is_next_three and is_next_five:
        return False

    return is_next_three or is_next_five


# 25. Write a Python program to check whether a given array of integers contains two 6's next to each other,
# or there are two 6's separated by one element, such as [6, 2, 6].

def contains_number(numbers):
    index_of_six = numbers.index(6)
    return numbers[index_of_six] == numbers[index_of_six + 1] or numbers[index_of_six] == numbers[index_of_six + 2]


# 26. Write a Python program to check whether there is a 2 in the array with a 3 somewhere
# later in a given array of integers.

def check_in_array(numbers):
    if len(numbers) >= 2 and 3 in numbers[numbers.index(2):]:
        return True
    return False


# 27. Write a Python program to convert an array into an index hash.

def convert_to_dict(numbers):
    return {k: None for k in numbers}


# 28. Write a Python program to find most occurred item in an given array.


def find_most_occurred(numbers):
    print(f"Original array: {numbers}")
    return {k: numbers.count(k) for k in numbers}


# 29. Write a Python program to check whether all items are identical in a given array.

def check_if_identical(numbers):
    print(f'Original array: {numbers}')
    print('If all items identical?')
    return len(set(numbers)) == 1


# 30. Write a Python program to search items start with specified string of a given array.


def search_items(strings, string_start):
    print(f'Original array: {strings}')
    print(f'Search items start with {string_start}: ')
    return [string for string in strings if string.startswith(string_start)]


# 31. Write a Python program to iterate an array starting from the last element.

def reverse_iterate(numbers):
    print(f'Original array: {numbers}')
    for number in numbers[::-1]:
        print(number)


# 32. Write a Python program to iterate over the first n elements of an given array.

def iterate_over_n_elements(numbers, n):
    print(f'Original array: {numbers}')
    print(f'First {n} elements')
    return numbers[:n]


# 33. Write a Python program to sort an given array of strings by length.

def sort_by_length(strings):
    strings.sort(key=lambda string: len(string))
    return strings


# 34. Compress the array, and removing all 0 from it and fill in the elements freed on the right side with the values -1

def compress_array(numbers):
    original_len = len(numbers)
    for number in numbers:
        if number == 0:
            numbers.remove(number)
    while len(numbers) != original_len:
        numbers.append(-1)
    return numbers


# 35. Convert the array so that the first go all negative elements, and then positive (0 is considered positive)

def convert_array(numbers):
    converted_numbers = []
    while numbers:
        min = numbers[0]
        for number in numbers:
            if number < min:
                min = number
        converted_numbers.append(min)
        numbers.remove(min)
    return converted_numbers


# 36. Write a program where a need to counts the number of times a number appear in an array.

def count_numbers(numbers):
    counted_numbers = {k: numbers.count(k) for k in numbers}
    for k, v in counted_numbers.items():
        print(f"{k} appears - {v} times.")


# 37. In a two-dimensional array of order M and N, swap the specified columns.

def swap_columns(numbers, column):
    numbers[0][column], numbers[1][column] = numbers[1][column], numbers[0][column]
    return numbers


# 38. Given the single-mass array with predefined values with a size of 10 items.
# Show on the screen array, and find the values that are repeated two and more times.

def repeated_numbers(numbers):
    print(numbers)
    if len(numbers) == 10:
        return list({number for number in numbers if numbers.count(number) >= 2})


# 39. Given the single-mass array with predefined values with a size of 10 items.
# Show on the screen array, and find the value that is the smallest nonpaired number.

def find_smallest_nonpaired(numbers):
    print(numbers)
    return min(number for number in numbers if number % 2 != 0)


# 40. Given the single-mass array. Cyclically shift the array on the K elements, on the right or left side.

def right_shift(numbers, k):
    print("Right Shift: ")
    for _ in range(k):
        return numbers[len(numbers) - k:] + numbers[:len(numbers) - k]


def left_shift(numbers, k):
    print("Left Shift: ")
    for _ in range(k):
        return numbers[k:] + numbers[:k]


def shift_array(numbers, k):
    print(f"Original array: {numbers}")
    print(right_shift(numbers, k))
    print(left_shift(numbers, k))
