import random
from hangman_parts import parts
from time import sleep
words = ["hangman", "programs", "language", "python", "encyclopedia", "apples"]
picked_word = random.choice(words)
print(picked_word)
print("Let me think of a word for you!")

def wait():
    for i in range(5):
        print('.', end=' ')
        sleep(.7)
    print()
wait()
print(f"The word has {len(picked_word)} letters.")

rightly_guessed_letters = ['_'] * len(picked_word)
wrongly_guessed_letters = []

def update():
    for i in rightly_guessed_letters:
        print(i, end=' ')
    print()
update()
parts(len(wrongly_guessed_letters))
while True:
    print("------------------------------------------------------------")
    guess = input("guess a letter: ")
    if guess in picked_word:
        index = 0
        for i in picked_word:
            if i == guess:
                rightly_guessed_letters[index] = guess
            index += 1
        update()
    else:
        if guess not in wrongly_guessed_letters:
            wrongly_guessed_letters.append(guess)
            parts(len(wrongly_guessed_letters))
        else:
            print("u already guessed that")
            print(wrongly_guessed_letters)
    if len(wrongly_guessed_letters)>=4:
        print("you lose!")
        print(f"I picked {picked_word}.")
        break
    if '_' not in rightly_guessed_letters:
        print("you win!")
        break
