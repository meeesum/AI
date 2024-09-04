import random

def find_numbers():
    for i in range (1500, 2701):
        if i % 7 == 0 and i % 5 == 0:
            print(i, " ")
def temp_convert(temp, flag):
    if flag == 0:
        f = (temp/5 * 9) + 32
        return f
    elif flag == 1:
        c = ((temp - 32 ) / 9) * 5
        return c
    
def number_guess(n):
    rand = random.randint(1,9)
    if rand == n:
        print("Well Guessed!")
    else:
            print("Try Again!")
            return 0

def reverse_word(word):
    s1 = ""
    print(s1)
    for i in range(len(word)-1, 0, -1):
        s1 = s1 + word[i]
    return s1
def count_even_odd(list):
    even_counter = 0
    odd_counter = 0
    for i in range (0,len(list)):
        if list[i] % 2 == 0:
            even_counter+=1
        elif list[i] % 2 != 0:
            odd_counter+=1
    print("The even count is " ,even_counter)
    print("The odd counter is ", odd_counter)

def print_list(list):
    for i in range (0, len(list)):
        print(list[i])
        print(type(list[i]))
# print("Choose from following")
# print("1. Celsuis to Fahrenheit")
# print("2. Fahrenheit to Celsius")
# choice = int(input())
# temp = float(input(print("Enter the temperature")))
# if choice == 1:
#     flag = 0
# elif choice == 2:
#     flag = 1

# print(temp_convert(temp, flag))
# find_numbers()

# n1 = 0
# while(n1 == 0):
#     n = int(input(print("Enter any number")))
#     n1 = number_guess(n)

# for i in range (1,6):
#     for j in  range (1, i+1):
#         print("*" , end = " ")
#     print("\n" , end= "")

# word = "meesum"
# print(reverse_word(word))

list = [[1452, 11.23, 1+2j], True, 'w3resource', (0,-1), [5, 12], {"class " : 'V', "section" : 'A'}]
# count_even_odd(list)
print_list(list)

for i in range (0,7):
    if i == 3 or i == 6:
        continue
    else:
        print(i)

for i in range (1,51):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)