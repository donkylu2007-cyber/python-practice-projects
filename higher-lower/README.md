# Higher Lower Game

A command-line guessing game written in Python, built while following the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp*.

The game shows two famous people or brands, and the player guesses which one has more social media followers. Each correct answer adds one point, and the game ends at the first wrong answer.

## How to run

Requires Python 3. Keep all three files in the same folder:

- `main.py` – the game logic
- `art.py` – the ASCII logo and "VS" art
- `game_data.py` – the list of accounts and their follower counts

```bash
python3 main.py
```

## What I practised

- Importing data and functions from other files (modules)
- Working with a list of dictionaries
- Generating random numbers with the `random` module, and making sure the two choices are different
- Using a `while` loop to keep the game running and track the score
