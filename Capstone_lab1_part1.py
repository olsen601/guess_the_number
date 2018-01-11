from random import randint

answer = randint(1,11)

guess = input("Guess a number between 1 & 50:")

g = int(guess)

while g != answer:
    print("guess again")

    if g > answer:
        print("too high")

    elif g < answer:
        print("too low")

    guess = input("Guess a number between 1 & 50:")
    g = int(guess)

print("correct!")
