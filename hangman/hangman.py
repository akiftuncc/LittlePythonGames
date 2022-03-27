from wordsforhangman import data
import random

i = random.randint(0,2465)
word_with_uppercase = data[i].upper()
word = list(word_with_uppercase)
lives = 6
guessed_letter_list = []
secretWord = len(word) * "-"
secretWord_list = list(secretWord)
we = 1
while lives > 0 and we == 1:
    test = 0
    metin = ""
    for i in secretWord_list:
        metin= metin+i+" "

    
    print("\t The Word: ",metin,end = "")
    guessed_letter = input("\tGuess A Word: ").upper()


    requirmentOfNestStep = 0
    for i in guessed_letter_list:
        if guessed_letter == i:
            requirmentOfNestStep = 1
            print("You already chose that letter! ")
    
    if requirmentOfNestStep == 0:
        guessed_letter_list.append(guessed_letter)
        q = 0
        j = -1
        for i in word:
            j+=1
            if guessed_letter == i:
                test = 1
                secretWord_list[j] = guessed_letter

        if test == 0:
            lives-=1
            print("Wrong Answer! Remaining lives: ",lives)

    we = 0    
    for i in secretWord_list:
        if i == "-":
            we = 1

if we == 0:
    print("You Win!","\tThe word was:",word_with_uppercase)

else:
    print("You Lose!","\tThe word was:",word_with_uppercase)









        


    

    






