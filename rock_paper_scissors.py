import random

options = ("Rock", "Paper", "Scissors")
running = True

print("🎮 Rock Paper Scissors Game")

while running:
    player = None
    computer = random.choice(options)

    # Get player choice
    while player not in options:
        player = input("Enter a choice (Rock/Paper/Scissors): ").title()

    print(f"\nPlayer: {player}")
    print(f"Computer: {computer}\n")

    # Game logic
    if player == computer:
        print("It's a tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You win!")
    elif player == "Paper" and computer == "Rock":
        print("You win!")
    elif player == "Scissors" and computer == "Paper":
        print("You win!")
    else:
        print("You lose!")

    # Play again
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("\nThanks for playing!")
