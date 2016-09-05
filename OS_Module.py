'''
Created on Sep 4, 2016

@author: Sudeep
'''
#Printing the list of files in the current location
import os

#As a list
print(os.listdir())

#As each item in a list
for x in os.listdir():
    print(x)
