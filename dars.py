# 1-masala
"""
def print_primes(n):
   
    print("Tub sonlar:")
    for i in range(2, n+1):
        if is_prime(i):
            print(i)

def is_prime(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Qaysi songa qadar tub sonlarni bilishni istaysiz? "))

print_primes(num)
"""
# 2-masala
"""
import math

def round_up_or_down(num):
    
    fractional_part = num - math.floor(num)
    if fractional_part > 0.5:
        return math.ceil(num)
    else:
        return math.floor(num)

numbers = [3.2, 4.7, 1.9, 7.1, 2.5]

rounded_numbers = list(map(round_up_or_down, numbers))

print("Asl list:", numbers)
print("Yaxlitlangan list:", rounded_numbers)
"""
# 3-masala
"""
import math

def get_integer_part(num):
    
    return math.floor(num)

numbers = [3.2, 4.7, 1.9, 7.1, 2.5]

integer_parts = list(map(get_integer_part, numbers))

print("Asl list:", numbers)
print("Butun qismlar:", integer_parts)
"""
# 4-masala
"""
def transform_number(num):
    
    if num > 0:
        return -num
    else:
        return 2 * num

numbers = [3, -4, 2, -1, 5]

transformed_numbers = list(map(transform_number, numbers))

print("Asl list:", numbers)
print("O'zgartirilgan list:", transformed_numbers)
"""
# 5-masala
"""
def is_greater_than_cube(num, N):
    
    return num > N ** 3

N = 2
numbers = [1, 3, 5, 7, 9, 11, 13]

greater_than_cube = list(filter(lambda x: is_greater_than_cube(x, N), numbers))

print(f"N = {N}")
print("Asl list:", numbers)
print(f"N^3 = {N**3}")
print(f"N^3 dan katta sonlar: {greater_than_cube}")
"""
# 6-masala
"""
def is_integer(num):
    
    return isinstance(num, int)

numbers = [3.14, 2.71, 1, 4, -5, 2.0, 7.0, -8, 9]

integers = list(filter(is_integer, numbers))

print("Asl list:", numbers)
print("Butun sonlar:", integers)
"""
# 7-masala
"""
def is_prime(num):
    
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = list(filter(is_prime, numbers))

print("Asl list:", numbers)
print("Tub sonlar:", primes)
"""
# 8-masala
"""
def is_string(element):
    
    return isinstance(element, str)

mixed_list = [1, 2.3, "apple", True, "banana", 4, "cherry", 5.6, "date"]

strings = list(filter(is_string, mixed_list))

print("Asl list:", mixed_list)
print("String elementlar:", strings)
"""
# 9-masala
"""
def is_positive(num):
    
    return num > 0

numbers = [-5, 0, 3, -2, 7, -1, 4, 6]

positive_numbers = list(filter(is_positive, numbers))

print("Asl list:", numbers)
print("Musbat sonlar:", positive_numbers)
"""
# 10-masala
"""
def convert_to_float(num):
   
    return float(num)

def convert_to_int(num):
    
    return int(num)

mixed_numbers = [1, 2.3, 4, 5.6, 7, 8.9]

int_to_float = list(map(convert_to_float, [int(x) for x in mixed_numbers if isinstance(x, int)]))
float_to_int = list(map(convert_to_int, [x for x in mixed_numbers if isinstance(x, float)]))

print("Asl list:", mixed_numbers)
print("Butun sonlar float qiymatga o'zgartirildi:", int_to_float)
print("Float sonlar butun songa yaxlitlandi:", float_to_int)
"""
# 11-masala
"""
bool_list = [1, 0, 1, 0, 1, 1, 0]

converted_list = list(map(bool, bool_list))

print("Asl list:", bool_list)
print("O'zgartirilgan list:", converted_list)
"""