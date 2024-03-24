while True:
    import random as rn

    lower = int(input("Enter lower limit : "))
    upper = int(input("Enter upper limit : "))

    if lower > upper:
        lower, upper = upper, lower
    random = rn.randrange(lower, upper + 1)

    limit = 0
    while limit < 10:
        guess = int(input("Guess the number : "))
        limit += 1

        if guess == random:
            print("Congratulation! You have finally guessed right. The number is", guess)
            print()
            break
        elif guess < random:
            print("You guessed smaller number.")
        elif guess > random:
            print("You guessed larger number.")
        if limit == 10:
            print("Oh! Seems you have exhausted the all limits. You can restart the game.")
            print("the number is", random)
            print("I think you can't win this game. :-D")
        print("\n")

print("Game is Ended!")