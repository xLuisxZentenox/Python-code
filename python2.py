#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
import os
os.system ('cls')

def pass_break():
    global pass_Break
    pass_Break = input('Do you want to try again? >> y/n: ')

def end_message():
    print("Thanks you!,Bye")

while True:
    n = int(input("Enter an integer: "))
    if n % 2 == 0:
        print(f'{n} is an even number')
        pass_break()
        if pass_Break == 'n':
            end_message()
            break
    else:
        print(f'{n} is odd')
        pass_break()
        if pass_Break == 'n':
            end_message()
            break