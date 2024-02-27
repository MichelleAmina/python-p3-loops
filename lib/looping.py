#!/usr/bin/env python3

def happy_new_year():
    i = 11
    while i > 0:
        i += -1
        print(i)
    print("Happy New Year!")

#happy_new_year()

def square_integers(int_list):
    # code goes here!
    square_list = [num * num for num in int_list]
    return square_list


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)








