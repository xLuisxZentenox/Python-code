import os
os.system('cls')
#1.----Realizar un programa que imprima en pantalla los números del 1 al 100.----
def numbers():
    for i in range(1,100+1):
        print(i)
    

#2.----Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno en uno.
def num():
    n=int(input("Enter a positive number: "))
    for i in range(1,n+1):
        print(i)

#3.----3. Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.
def values_10():
    sum=0; avg=0
    for i in range(10):
        n=int(input("Enter a number: "))
        sum+=n
        avg=sum/10
    print('----------------------------------')
    print(f'''sum: {sum} 
average: {avg}
    ''')

'''4.---Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar
 y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté
comprendida en el rango de 1.20m y 1.30m son aptas. Imprimir por pantalla la cantidad de
piezas aptas que hay en el lote.'''

def pieces():
    suitables=0; lenghts=[]
    piece=int(input("Enter the number of parts to be processed: "))
    for i in range(piece):
        lenght=float(input("Enter the lenght of the parts:  "))

        if lenght >=1.20 and lenght<=1.30:
            suitables+=1
            lenghts.append(lenght)
    print('----------------------------------------------------------')
    print(f'''Suitable pieces: {suitables} 
lenghts: {lenghts} ''')