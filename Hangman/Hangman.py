'''
Hangman.py

Ariana Fairbanks
'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
    
        file = open('words.txt','r')
        
        '''
        file = open(sys.argv[1], 'r')
        '''
        
        self.words = []
        self.wordguess = []
        self.guessed = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c + " ",end="")
        print()



    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        self.wordguess = ['_'] * len(word)
        self.printword()
        guesses = 0
        
        while guesses < 10:
            print()
            ch = input('Enter a guess:').lower()
            if(len(ch) != 1):
                print("Only one character is allowed in each input.")
            elif(ch.isalpha() == False):
                print("Only allow alphabetic characters.")
            elif(ch in self.guessed):
                print("The letter " + ch + " has already been used.")
            else:
                self.guessed.append(ch)
                check = list(map(lambda crntLetter : ch == crntLetter, word))
                contained = False
                i = 0
                while(i < len(check)):
                    if(check[i] == True):
                        contained = True
                        self.wordguess[i] = word[i]
                    i += 1
                
                if(contained == False):
                    print()
                    print(ch + " does not occur.")
                    guesses += 1

                print()
                self.printword()
                print()

                if(''.join(self.wordguess) == word):
                    guesses = 11
                    print("Congratulations!")
                else:
                    print(str(guesses) + " incorrect guesses")
                
        
        if(guesses == 10):
            print("Sorry dude, the word is " + word + ".")
        
        

if __name__ == "__main__":

    game = Hangman()

    game.playgame()
