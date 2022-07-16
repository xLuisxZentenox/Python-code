'''En una empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación pueden ser 0.0, 0.4, 0.6 o más
pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
La cantidad de dinero conseguida en cada nivel es de $2.400 multiplicada por la puntuación del nivel.

Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa con listas (sin diccionarios) que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.'''

import os
os.system ('cls')

#-----lIST------------------------------------------------------------------------
names = []; salarys = []; scores = []; rewards = []; total = []

#-----FUNCTIONS-------------------------------------------------------------------

def user_data():

    global name, score,reward,salary

    name = input("Type your name: ").upper() 
    names.append(name)

    salary = float(input('Enter your salary $ '))
    salarys.append(salary)

    score = float(input('Enter your score (ENTER ONLY -> 0.0, 0.4, 0.6 or +): ')) 
    scores.append(score)

    reward = 2400

def pass_break():
    global pass_Break
    pass_Break = input('Do you want to try again? >> y/n: ')
    separator()

def separator():
    print('-------------------------------------------------------------')

def validation():
    global money_rewarded,total_salary
    if score == 0.0:
        print(f'{name} YOUR SCORE IS UNACCEPTABLE, YOU HAVE NO REWARD')

    if score == 0.4:
        money_rewarded = reward *  0.4
        rewards.append(money_rewarded)

        total_salary = salary + money_rewarded
        total.append(total_salary)

        print(f'{name} YOUR LEVEL IS ACCEPTABLE, YOUR REWARD IS ${money_rewarded}')

    if score == 0.6:
        money_rewarded = reward * 0.6
        rewards.append(money_rewarded)

        total_salary = salary + money_rewarded
        total.append(total_salary)

        print(f'{name} YOUR LEVEL IS MERITORIOUS, YOUR REWARD IS ${money_rewarded}')

    if score > 0.6:
        money_rewarded = reward * score
        rewards.append(money_rewarded)

        total_salary = salary + money_rewarded
        total.append(total_salary)
        print(f'{name} YOUR LEVEL IS MERITORIOUS, YOUR REWARD IS ${money_rewarded}')

    if score >0.0 and score < 0.4:
        print('INVALID SCORE')
    if score >0.4 and score <0.6:
        print('INVALID SCORE')

def main():
    print('''.::. ENTERPRISE REWARDS SIMULATOR .::.
    (1) ENTER USER DATA AND SCORE
    (2) SHOW RESULTS
    (0) EXIT
    ''')

#Main
while True:
    main()
    option = int(input('Choose an option (Type 1, 2 or 0): '))

    #---ENTER DATA---
    if option == 1:
        separator() #-----line separation-----
        user_data()
        separator() #-----line separation-----
        validation()
        pass_break()
        if pass_break=='n':
            break

     #---SHOW RESULTS---
    if option == 2:
        print(f'''.::. TOTAL REWARDS .::. '
        NAME: {names}
        SALARY: {salarys}
        SCORE: {scores}
        REWARD: ${rewards}
        TOTAL SALARY: {total}
        ''')
        pass_break()
        if pass_Break == 'n':
            break

    #---EXIT---
    if option == 0:
        break