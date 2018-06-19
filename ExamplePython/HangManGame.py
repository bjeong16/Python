import string
from string import maketrans
import random

def startGame(question):
    tries = len(question) * 3
    currentState = "_"*len(question)
    while tries != 0:
        print(currentState)
        option = raw_input("To guess the entire word, press 1 \n To guess a letter in the word press 2 \n To give up and see the word press 3 \n")
        if option == 1:
            guess = raw_input("Please enter your guess: \n")
            if guess == question:
                print("Congratulations, you have saved Hangman")
            else:
                print("That is not the write word. You now have " + str(tries - 1) + "chances left \n")
                tries -= tries
        if option == 2:
            guess = raw_input("Please enter a character: \n")
            for letter in question:
                if guess == option:

        if option == 3:
            print(question)





if __name__ == '__main__':
    print("Welcome to HangMan.")
    text_file = open("Dict.txt", 'r')
    mysteryWord = text_file.read()
    mysteryWord = mysteryWord.split()
    mysteryWord = mysteryWord.translate(None, "\n")

    for word in mysteryWord:
        length = len(word)
        if length < 5:
            mysteryWord.translate(word, "")

    count = len(mysteryWord)
    index = random.randint(0, count)
    question = mysteryWord[index]
    count = len(question)

    for x in range(count):
        print("_ ")

    print("There are " + str(count) + "letters in the word")
    print("You get" + str(count*3) + "tries to guess the word")

    startGame(question)



