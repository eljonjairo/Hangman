# Hangman code
# John Diaz
# January 2023 Base on 12 beginner Python projects - Coding Course FreeCodeCamp.org
# TO DO list:
# words by categories
#
# 

import random
from words import words 
import string

def CheckValidWords(words):
    # Remove invalid words from the list
    rwords = 0
    for word in words:
        if( '-' in word or '_' in word or ' ' in word):
            words.remove(word)
    
    return words


# Select the valid words from the list
words = CheckValidWords(words)
# Python is case dependent, put everything in uppercase
word = random.choice(words).upper()     # Randomly chooses a word from the list

nlet = len(word)                        # Number of letters in word
guessList = []                       # list the letters guessed by user
print(word)

print(f" The word to guess has {nlet} letters.")
print( " You have 10 lives, let start !!!!")

guess = True
lives = 10

mlet = 0                                 # Number of correct letters
while guess and lives > 0:
   
    print() 
   
    print(" You have tried: ", ' '.join(guessList))
    Let = input(f" guess a letter: ").upper()
    # Check the user insert 1 caracter
    if len(Let) == 1 :
       # Check the user insert a letter 
       if Let.isalpha():
           if Let in guessList:
               print(f" you already tried {Let}...")
               
           guessList.append(Let)
           
           # Check the letter is in word
           if Let in word:
               # Count the times Let is in word
               np = word.count(Let)
               mlet += np
         
               if mlet == nlet:
                   guess = False
           else:
               lives -= 1
       else:
           lives -= 1
           print(f" {Let} it\'s not a letter !! ") 
    else:
        lives -= 1
        print(" Insert just one letter !!")

    wstr = [ letter if letter in guessList else '_' for letter in word]
    print()
    print(f" Lives: {lives}")
    print(" Current Word: "," ".join(wstr))  # Create a string separatign with " " the caracters in wstr
   

print()
print(f" The word is: {word}")
print()
if guess:
    print( " Sorry, you lost, start again....")
else:
    
    print( " Congratulations !!!!")

