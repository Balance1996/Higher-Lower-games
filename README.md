# Higher Lower Game

## Project Overview

This project is a Python implementation of the Higher Lower guessing game. The player compares two contenders, A and B, and guesses which one has more followers.

A represents the current contender, while B represents the challenger. Each correct guess increases the player's score. An incorrect guess ends the game, and the final score reflects the number of correct guesses accumulated.

## Project Versions

### 1. `HL_projectremdic.py`

This version removes a dictionary entry from `HL_dic` after a correct guess, preventing that entry from being used again. The dataset contains 20 entries.

With the game starting with two contenders and consuming an entry after each successful round, the maximum score is 19, provided each remaining round has a valid challenger.

### 2. `HL_tutorial.py`

This version explores the Higher Lower mechanics without removing entries from the original dataset. It selects new challengers while keeping the dataset intact.

## What I Learned

One of the most challenging aspects of this project was managing state transitions and coordinating function calls within the `main()` loop.

The project gave me practice with:
- Conditional logic (`if`, `elif`, and `else`)
- `while` loops
- Functions and return values
- Random selection using `random.choice()`
- Variable reassignment and state transitions
- Selecting eligible challengers based on follower counts

## How to Run

1. Make sure Python is installed.
2. Open the project in a Python editor, such as Thonny.

##Guidance for anti-dup codes and trace states
-it is coordinated with codes from get_challenger(contender) in 'H_projectremdic.py or available_contender(contender)
-if you want to understand trace state use this file as reference 'HL_traceguide.py'
4. Run the relevant Python file.

I used Thonny to develop and debug the program.
