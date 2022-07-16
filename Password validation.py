'''Escribir un programa donde el usuario almacene una contraseña en una variable y luego indique al usuario 
que la ingrese nuevamente e imprima por pantalla si la contraseña introducida por el usuario 
coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

import os
os.system ('cls')

import getpass
def separator():
    print('--------------------------------------------')

def names():
    global name
    name = input("Type your name: ").title()

def show_passw():
    show_pass = input("Show password -> y/n: ")
    separator()
    if show_pass == 'y':
        print(f"Your password: {passw}")
        separator()

def password():
    global passw
    passw = getpass.getpass("Enter a password: ").lower()
    show_passw()
    

def validation():
    global passw_val
    passw_val = getpass.getpass("Enter your password again: ")
    show_passw()

#Main
while True:
    print('''CREATE A USER''')
    names()
    password()
    break
while True:
    validation()
    if passw_val == passw:
        print(f"{name} your password has been successfully created!")
        break
    else:
        print("Passwords do not match,try again")

