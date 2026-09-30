import random


def number_guessing_game():

    print("===================================")
    print("       NUMBER GUESSING GAME")
    print("===================================")

    name = input("Enter your name: ").strip()

    if name == "":
        name = "Player"

    games_played = 0
    games_won = 0
    games_lost = 0
    high_score = 0
    best_attempts = 0

    while True:

        print("\n===================================")
        print("          DIFFICULTY LEVEL")
        print("===================================")
        print("1. Easy   (1 - 50, 15 attempts)")
        print("2. Medium (1 - 100, 12 attempts)")
        print("3. Hard   (1 - 500, 10 attempts)")

        while True:
            difficulty = input("Choose difficulty: ").strip()

            if difficulty == "1":
                minimum = 1
                maximum = 50
                max_attempts = 15
                level = "Easy"
                break

            elif difficulty == "2":
                minimum = 1
                maximum = 100
                max_attempts = 12
                level = "Medium"
                break

            elif difficulty == "3":
                minimum = 1
                maximum = 500
                max_attempts = 10
                level = "Hard"
                break

            else:
                print("Invalid choice! Please select 1, 2 or 3.")

        secret_number = random.randint(minimum, maximum)
        attempts = 0
        score = 100

        games_played += 1

        print("\n===================================")
        print("             GAME START")
        print("===================================")
        print(f"Player: {name}")
        print(f"Difficulty: {level}")
        print(f"Range: {minimum} - {maximum}")
        print(f"Maximum Attempts: {max_attempts}")

        while attempts < max_attempts:

            try:
                guess = int(
                    input(
                        f"\nEnter your guess ({minimum}-{maximum}): "
                    )
                )

            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if guess < minimum or guess > maximum:
                print(
                    f"Please enter a number between "
                    f"{minimum} and {maximum}."
                )
                continue

            attempts += 1

            if guess == secret_number:

                print("\n===================================")
                print("             YOU WON")
                print("===================================")

                print(f"Player: {name}")
                print(f"Correct Number: {secret_number}")
                print(f"Attempts Used: {attempts}")

                if attempts == 1:
                    score = 100
                else:
                    score = max(
                        10,
                        100 - ((attempts - 1) * 8)
                    )

                print(f"Score: {score}")

                games_won += 1

                if score > high_score:
                    high_score = score

                if best_attempts == 0 or attempts < best_attempts:
                    best_attempts = attempts

                break

            elif guess < secret_number:
                print("Too Low!")

            else:
                print("Too High!")

            difference = abs(secret_number - guess)

            if difference <= 5:
                print("Hint: Very close!")

            elif difference <= 15:
                print("Hint: You are close.")

            elif difference <= 30:
                print("Hint: You are somewhat far.")

            else:
                print("Hint: You are far from the number.")

            if secret_number % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")

            score = max(10, score - 8)

        else:

            games_lost += 1

            print("\n===================================")
            print("            GAME OVER")
            print("===================================")

            print(f"Correct Number: {secret_number}")
            print(f"Attempts Used: {attempts}")
            print("Score: 0")

        print("\n===================================")
        print("           STATISTICS")
        print("===================================")

        print(f"Games Played : {games_played}")
        print(f"Games Won    : {games_won}")
        print(f"Games Lost   : {games_lost}")

        if games_played > 0:
            win_rate = (games_won / games_played) * 100
        else:
            win_rate = 0

        print(f"Win Rate     : {win_rate:.2f}%")
        print(f"High Score   : {high_score}")

        if best_attempts == 0:
            print("Best Attempts: No win yet")
        else:
            print(f"Best Attempts: {best_attempts}")

        print("\n===================================")
        print("1. Play Again")
        print("0. Exit")
        print("===================================")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("\nThank you for playing!")
            print(f"Total Games Played: {games_played}")
            print(f"Total Games Won: {games_won}")
            print(f"High Score: {high_score}")
            break

        elif choice == "1":
            continue

        else:
            print("Invalid choice!")
            print("Game is closing.")
            break


number_guessing_game()