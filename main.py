# Pythagoras' pants
# Module name: Task_1

from array import *

def main():
    print_hi()
    pythagorean_pants()

def pythagorean_pants():
    # Create an array of unsorted numbers.
    arr_int = []
    filling_an_array(arr_int)
    a = arr_int[0] ** 2
    b = arr_int[1] ** 2
    c = arr_int[2] ** 2
    if (a + b == c) or (a + c == b) or (b + c == a):
        print(str(arr_int) + ' -> True')
    else:
        print(str(arr_int) + ' -> False')

def filling_an_array(arr_int):
    # Filling the array with verified data
    for i in range(3):
        user_input = input('Введи ' + str(i+1) + ' елемент списка: ')
        ver_number = get_number(i, user_input, arr_int)
        arr_int.append(ver_number)

def get_number(i, user_input, arr_int):
    # Сhecking entered numbers
    while True:
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть число.")
            user_input = input('Введи ' + str(i + 1) + ' елемент списка: ')


def print_hi():
    print(f'Привіт!')

if __name__ == '__main__':
    main()