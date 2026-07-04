secret_number = 42
attempts = 0
while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess > secret_number:
        print("Too High")
    elif guess < secret_number:
        print("Too Low")
    else:
        print("Correct!")
        print("Total Attempts:", attempts)
        break