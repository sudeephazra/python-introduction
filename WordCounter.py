'''
Created on Sep 7, 2016

@author: Sudeep
'''


#Q1 - Find the 10 most used words in a file

#A1.1
# Using by-hand methods
my_dict = {}
i=1
 
with open("WordCounter_SampleFile1", "r") as file:
   for line in file:
       words = line.split()
       word_counter = [a.lower() for a in words]
       for a in word_counter:
           my_dict[a] = 1 if a not in my_dict else my_dict[a] +1
           
list_words = sorted(my_dict, key=my_dict.get, reverse=True)

for list_word in list_words:
    print(list_word, my_dict[list_word])
    if (i<10):
        i+=1
    else:
        break

#A1.2        
# Using collections module
import collections
infile = open("WordCounter_SampleFile1")    
words = collections.Counter()
 
for line in infile:
    words.update(line.split())
                               
for word, count in words.items():
    print(word, count)
