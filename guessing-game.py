def main():
    print("PYTHON GUESSING GAME")
    answer = "fish"

    while True:
        print("I am thinking of an animal...")
        guess = str(input("What animal am I thinking of? "))
        guess=guess.lower()
        guess=guess.strip()

        if guess == answer:
            print("Nice! You guessed it!")
            break
        elif guess == "quit":
            print("You quit the game.")
            break
        else:
            print("Thats not it, guess again.")
    
main()


