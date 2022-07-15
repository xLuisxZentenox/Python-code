#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
import os
os.system ('cls')

def datos():
    global edad
    edad = int(input("Ingrese su edad: "))

def pass_breaker():
    global pass_break
    pass_break = input("Quiere intentarlo nuevamente) >> y/n: ")

def validacion():
    if edad >= 18:
        print(f"Usted tiene {edad} años, es mayor de edad")
    elif edad >=1 and edad <18:
        print(f"Usted tiene {edad} años, es menor de edad")
    else:
        edad 
        print("Porfavor ingrese un dato valido,intentelo nuevamente")
while True:
    datos()
    validacion()
    pass_breaker()
    if pass_break == 'n':
        break