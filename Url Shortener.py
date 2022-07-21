from distutils.errors import LinkError
import pyshorteners
import os
os.system('cls')

link = input("Enter link : ") #----Enter any link-----

#----Shortened url----
print(pyshorteners.Shortener().tinyurl.short(link)) #--shortened link displayed using "tinyUrl"service.You can use another shortener like: bitly or ow.ly.

#----Expanded url----
print(pyshorteners.Shortener().tinyurl.expand('https://tinyurl.com/23kfcmvn')) #--Enter the shortened link generated by the service to be extended.