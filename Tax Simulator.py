'''Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a $350.000 mensuales. 
Escribir un programa que pregunte al usuario su nombre, edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.'''

import os
os.system ('cls')

def data():
    global name, age, salary
    name = input("Type your name: "); age = int(input("Enter your age: ")); salary = int(input("Enter your monthly salary (example > 340000): "))

def pass_break():
    global pass_breaks
    pass_breaks = input('Do you want to consult again? >> y/n: ')
    print('------------------------------------------------------')

def separator():
    print('------------------------------------------------------')

def validation():
    if age >=18 and salary >=350000:
        print('VALID REQUIREMENTS, YOU HAVE TO PAY TAXES')
    if age >=18 and salary <350000:
        print('YOU DO NOT MEET THE MONTHLY SALARY REQUIEREMENTS')
    if age <18 and salary >=350000:
        print('YOU DO NOT MEET THE AGE REQUIREMENT')
    if age <18 and salary <350000:
        print('YOU DO NOT MEET ANY REQUIREMENTS')

#MAIN
while True:
    print('.:: TAX SIMULATOR ::.')
    data()
    separator()
    validation()
    separator()
    pass_break()
    if pass_breaks == 'n':
        print('Thanks You,Bye')
        break
