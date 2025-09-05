secret = 7 # Secret Variable

print("Welcome to the Guessing Game")   # Initial Greeting Message

# Infinitely running while loop
while True:
    # Take the guess number from the user input iteratively
    guess = int(input("Enter a number (Enter -1 to QUIT): "))

    # Break the loop of the guess matches secret value with the correct message
    if guess == secret:
        print("🎉 Correct!")
        break
    # Skip this iteration if the guess is less than -1
    elif guess < -1:
        print("Skipping Guess, Try Again")
        continue
    # Break the loop and exit the program if the guess is -1
    elif guess == -1:
        print("Quitting Game!")
        break
    # Re-iterate the loop from the beginning if the guess does not matches the secret with displaying the following message
    else:
        print("Wrong Guess, Try Again")
