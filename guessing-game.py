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
            likeIt = str(input("Do you like " + answer +"? ('y' or 'n')"))
            likeIt=likeIt.lower()
            likeIt=likeIt.strip()
            if likeIt == "y":
                print("Cool, I like " + answer + " too.")
            else:
                print("Oh... I suppose we cant all have good tastes.")
            break
        elif guess[0] == "q":
            print("You quit the game.")
            break
        else:
            print("Thats not it, guess again.")
    
main()


