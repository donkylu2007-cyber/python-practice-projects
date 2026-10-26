# Coffee Machine

A command-line coffee machine simulator written in Python, built while following the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp*.

## Features

- Order an espresso, latte or cappuccino
- Checks whether there is enough water, milk and coffee before making a drink
- Accepts coins (quarters, dimes, nickels, pennies), calculates the total and gives change
- Refunds the money if it is not enough
- `report` shows the remaining resources and the money earned
- `off` turns the machine off

## How to run

Requires Python 3.

```bash
python3 main.py
```

Example:

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters?: 12
how many dimes?: 0
how many nickels?: 0
how many pennies?: 0
Here is $0.5 in change.
Here is your latte ☕️. Enjoy!
```

## What I practised

- Nested dictionaries to store the menu and resources
- Splitting the program into small functions (checking resources, processing coins, making the drink)
- `while` loops, `if`/`elif`/`else` and the `global` keyword
