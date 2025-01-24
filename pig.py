import random


def roll_dice(min_value=1, max_value=6):
    return random.randint(min_value, max_value)


def get_player_count():
    while True:
        players = input("Enter the number of players (2 - 4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("Must be between 2 - 4 players.")
        else:
            print("Invalid input, try again.")


def game_turn(player_number, current_score):
    while input("Would you like to roll (y)? ").lower() == "y":
        roll_value = roll_dice()
        if roll_value == 1:
            print("You rolled a 1! Turn done!")
            return 0
        current_score += roll_value
        print(f"You rolled a: {roll_value}")
        print(f"Your score this turn is: {current_score}")
    return current_score


def main():
    players = get_player_count()
    max_score = 50
    player_scores = [0] * players

    while max(player_scores) < max_score:
        for i in range(players):
            print(f"\nPlayer {i + 1}'s turn!")
            print(f"Your total score is: {player_scores[i]}\n")

            player_scores[i] += game_turn(i + 1, 0)
            print(f"Your total score is: {player_scores[i]}")

    winner_index = player_scores.index(max(player_scores))
    print(f"\nPlayer {winner_index + 1} wins with a score of: {max(player_scores)}")


if __name__ == "__main__":
    main()