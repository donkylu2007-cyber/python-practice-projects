from art import logo
from art import vs
from game_data import data
from random import randint

print(logo)


def randint_except(low, high, exclude):
    """Returns a random integer between low and high that is not equal to exclude."""
    while True:
        rand_val = randint(low, high)
        if rand_val != exclude:
            return rand_val


def game():
    continue_game = True
    score = 0
    while continue_game:
        # generate answer
        a = randint(0, len(data) - 1)
        b = randint_except(0, len(data) - 1, a)
        compare_a = data[a]
        against_b = data[b]
        if compare_a['follower_count'] > against_b['follower_count']:
            answer = "a"
        else:
            answer = "b"

        # start game
        print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
        print(vs)
        print(f"Against B: {against_b['name']}, {against_b['description']}, from {against_b['country']}")
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        # answer check
        if user_answer == answer:
            score += 1
            print("")
            print(f"You're right! current score: {score}")
        else:
            continue_game = False
            print(f"Sorry that's the wrong answer. Final score {score}")


game()
