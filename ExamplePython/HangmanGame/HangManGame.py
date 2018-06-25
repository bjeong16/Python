import string
from string import maketrans
import random

def startGame(question):
    tries = len(question) * 3
    currentstate = list()
    for x in question:
        currentstate.append("_")
    while tries != 0:
        print("You now have " + str(tries) + " tries left")
        print(currentstate)
        option = input("To guess the entire word, press 1 \nTo guess a letter in the word press 2 \nTo give up and see the word press 3 \n")
        if option == 1:
            guess = raw_input("Please enter your guess: \n")
            if guess == question:
                print("Congratulations, you have saved Hangman")
                return
            else:
                print("That is not the right word. You now have " + str(tries - 1) + "chances left \n")
                tries -= 1
        if option == 2:
            guess = raw_input("Please enter a character: \n")
            counter = 0
            for letter in question:
                if guess == letter:
                    currentstate[counter] = letter
                counter += 1
            tries -=1
        if option == 3:
            print(question)
            print("Hangman Died")
            return

    print("Hangman Died")
    print("The correct answer was: " + question)
    return




if __name__ == '__main__':
    print("Welcome to HangMan.")
    text_file = open("Dict.txt", 'r')
    mysteryWord = text_file.read()
    mysteryWord = mysteryWord.split()
    for word in mysteryWord:
        length = len(word)
        if length < 5:
            mysteryWord.remove(word)

    count = len(mysteryWord)
    index = random.randint(0, count)
    question = mysteryWord[index]
    count = len(question)

    for x in range(count):
        print("_ ")

    print("There are " + str(count) + " letters in the word")
    print("You get " + str(count*3) + " tries to guess the word")

    startGame(question)



