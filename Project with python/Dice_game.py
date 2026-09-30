import random


def dice_game():

    print("================================")
    print("      DICE GAME    ")
    print("================================")

    # Player Names
    player1 = input("Enter First Player Name: ").strip()
    while player1 == "":
        print("Name cannot be empty!")
        player1 = input("Enter First Player Name: ").strip()

    player2 = input("Enter Second Player Name: ").strip()
    while player2 == "":
        print("Name cannot be empty!")
        player2 = input("Enter Second Player Name: ").strip()

    rounds = 5

    # Win Counter
    player1_wins = 0
    player2_wins = 0
    draws = 0

    while True:

        # Reset score for new game
        score1 = 0
        score2 = 0

        # Statistics
        highest1 = 0
        highest2 = 0
        total_rolls1 = 0
        total_rolls2 = 0

        print("\n================================")
        print("          START GAME")
        print("================================")

        # 5 Rounds
        for i in range(1, rounds + 1):

            print(f"\n---------- ROUND {i} ----------")

            # ---------------- PLAYER 1 ----------------
            input(f"{player1}'s turn - Press Enter to roll: ")

            dice1 = random.randint(1, 6)

            print(f"{player1} rolled: {dice1}")

            score1 += dice1
            total_rolls1 += 1

            # Highest roll
            if dice1 > highest1:
                highest1 = dice1

            # Bonus for 6
            if dice1 == 6:
                score1 += 2
                print("BONUS! +2 points")

            # ---------------- PLAYER 2 ----------------
            input(f"{player2}'s turn - Press Enter to roll: ")

            dice2 = random.randint(1, 6)

            print(f"{player2} rolled: {dice2}")

            score2 += dice2
            total_rolls2 += 1

            # Highest roll
            if dice2 > highest2:
                highest2 = dice2

            # Bonus for 6
            if dice2 == 6:
                score2 += 2
                print("BONUS! +2 points")

            # ---------------- ROUND RESULT ----------------
            print("\n===== ROUND RESULT =====")

            print(f"{player1}: {dice1}")
            print(f"{player2}: {dice2}")

            if dice1 > dice2:
                print(f"Round Winner: {player1}")

            elif dice2 > dice1:
                print(f"Round Winner: {player2}")

            else:
                print("Round Draw!")

            print("------------------------")
            print(f"{player1} Total Score: {score1}")
            print(f"{player2} Total Score: {score2}")

        # ---------------- FINAL RESULT ----------------

        print("\n================================")
        print("        FINAL RESULT")
        print("================================")

        print(f"{player1} Score: {score1}")
        print(f"{player2} Score: {score2}")

        # Winner
        if score1 > score2:

            print(f"\n{player1} WINS THE GAME!")
            player1_wins += 1

        elif score2 > score1:

            print(f"\n{player2} WINS THE GAME!")
            player2_wins += 1

        else:

            print("\nGAME DRAW!")
            draws += 1

        # ---------------- STATISTICS ----------------

        print("\n================================")
        print("        PLAYER STATISTICS")
        print("================================")

        print(f"\n{player1}")
        print(f"Total Rolls : {total_rolls1}")
        print(f"Highest Roll: {highest1}")
        print(f"Final Score : {score1}")

        print(f"\n{player2}")
        print(f"Total Rolls : {total_rolls2}")
        print(f"Highest Roll: {highest2}")
        print(f"Final Score : {score2}")

        # ---------------- WIN COUNTER ----------------

        print("\n================================")
        print("          SCOREBOARD")
        print("================================")

        print(f"{player1} Wins : {player1_wins}")
        print(f"{player2} Wins : {player2_wins}")
        print(f"Draws      : {draws}")

        # ---------------- PLAY AGAIN ----------------

        print("\n================================")
        print("1. Play Again")
        print("0. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            continue

        else:
            print("Invalid choice! Game will exit.")
            break

    # ---------------- GAME OVER ----------------

    print("\n================================")
    print("       THANK YOU FOR PLAYING!")
    print("================================")

    print(f"{player1} Total Wins: {player1_wins}")
    print(f"{player2} Total Wins: {player2_wins}")
    print(f"Total Draws: {draws}")

    print("\nGame Over!")


# Start Game
dice_game()