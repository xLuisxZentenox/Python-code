'''Escribir un programa donde el usuario almacene una contraseña en una variable y luego indique al usuario 
que la ingrese nuevamente e imprima por pantalla si la contraseña introducida por el usuario 
coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

import os
os.system ('cls')

def names():
    name = input("Type your name: ")

def password():
    global passw
    passw = input("Enter a password: ").lower()

def validation():
    global passw_val
    passw_val = input("Enter your password again: ")

#Main
while True:
    print('''CREATE A USER''')
    names()
    password()
    break
while True:
    validation()
    if passw_val == passw:
        print("Your password has been successfully created!")
        break
    else:
        print("Passwords do not match,try again")

