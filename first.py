print("================================")
print("      NUMBER GUESSING GAME      ")
print("================================")
secret_number = 25
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    guess = int(input("Enter your guess (1-50): "))
    attempts += 1
    if guess == secret_number:
        print("Congratulations! You guessed number is matched .")
        break
    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

    print("Attempts left:", max_attempts - attempts)

if attempts == max_attempts and guess != secret_number:
    print("Game Over!")
    print("The matched number was:", secret_number)
