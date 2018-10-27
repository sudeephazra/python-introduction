'''
Created on Aug 28, 2016

@author: Sudeep
'''
import os
import sys

people_dict = {'name':'Sudeep', 'age':121, 'job':'whatever i feel like', 'games':'[\'cricket\',\'tennis\']'}

#Length of the dictionary
print("Length of the dictionary -- ")
print(people_dict.__len__())
#Keys of the dictionary
print("Keys of the dictionary -- ")
print(people_dict.keys())
#Retrieve value for particular key
print("Retrieve value for particular key -- ")
print(people_dict.get('games'))

#Iterate over the values using he keys
print("Iterate over the values using the keys -- ")
for key in people_dict.keys():
    print('{} - {}'.format(key, people_dict.get(key)))