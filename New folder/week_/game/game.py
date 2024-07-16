import random

def main():
    level = get_level()
    lives = get_lives()
    secret = random.randint(1, level)

    i = lives
    while i > 0:
        try:
            guess = get_guess()
            if guess > secret:
                print("Too large!")
            elif guess < secret:
                print("Too small!")
            elif guess == secret:
                print("thats right.. you won")
                break
            i = i - 1
        except ValueError:
            print("gave me a number")
            continue
    if guess != secret:
        print("you lose")

def get_level():
    while True:
        try:
            x = int(input("level: "))
            if x > 0:
                return x
        except ValueError:
            print("gave me a number")

def get_guess():
    while True:
        try:
            a = int(input("guess: "))
            if a >= 0:
                return a
        except ValueError:
            print("gave me a number")

def get_lives():
    while True:
        try:
            a = int(input("lives: "))
            if a >= 0:
                return a
        except ValueError:
            print("gave me a number")
main()
