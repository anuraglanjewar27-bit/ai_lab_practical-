low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:

    guess = (low + high) // 2

    print("My Guess is:", guess)

    feedback = input("Enter (higher/lower/correct): ").lower()

    if feedback == "higher":
        low = guess + 1

    elif feedback == "lower":
        high = guess - 1

    elif feedback == "correct":
        print("Number Guessed Successfully!")
        break

    else:
        print("Invalid feedback!")

