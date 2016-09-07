'''
Created on Sep 4, 2016

@author: Sudeep
'''
#Printing the list of files in the current location
import os

#As a list
print(os.listdir())
print(os.getcwd()) 

#As each item in a list
for x in os.listdir():
    print(x)


#Create a File
with open("file", "w", encoding="utf-8") as myFileWrite:
    myFileWrite.write("Hola!!")
     
#This operation is not allowed as the file is closed outside the block    
# myFile.write("Hola!!")   

#Read from a file
with open("file", "r") as myFileRead:
    #Read the whole file as a string and print it
    print(myFileRead.read())
    
    #Read the file line by line
    for myFileReadLine in myFileRead:
        print(myFileReadLine)

    #Prints the entire file as a list    
    print(myFileRead.readlines())    
#No need to close the file as it is automatically closed   
        
        