import os
os.system('cls')

while True:
    cmd = 'netsh wlan show profile'
    result = os.popen(cmd)
    print(result.read())

    myfile = open('wifi.txt', 'a')

    ntw = input('Enter your network name: ')
    cmd2 = "netsh wlan show profile "+ntw+" key=clear"
    result2 = os.popen(cmd2)
    myfile.write(result2.read())
