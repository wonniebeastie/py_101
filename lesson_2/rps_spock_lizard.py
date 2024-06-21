# RPS Bonus Features
#
# PEDAC
#
# - UNDERSTAND THE PROBLEM -
#
# Objective: Add an additional two choices - Lizard & Spock - in the 
# ROCK PAPER SCISSORS game. X
#
# EXPLICIT RULES
#
# Shortened Input 
# - let users type "r" for "rock" and so on (Two inputs start with "s" 
# - how to resolve?). X
#
# Best of Five 
# - Keep track of player's wins and computer's wins. 
# - When either one reaches 3 wins, end match.
# - Don't add incrementing logic to `display_winner`.
#
# Game Rules:
# Scissors > Paper x
# Paper > Rock x
# Lizard > Spock x
# Spock > Scissors x
# Scissors > Lizard x
# Lizard > Paper x
# Paper > Spock x
# Spock > Rock x
# Rock > Scissors x
# 
# MENTAL MODEL:
# Update RPS game to include Spock & Lizard choices, keep track of the
# player's and computer's score, once either one reaches score of 3, 
# end game.

import random 
from helpers import prompt, shorthand_translate, display_winner

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

while True: 
    # Reset the scores for repeat games.
    computer_score = 0
    player_score = 0

    # Loop until either player or computer reaches 3 points.
    while player_score < 3 and computer_score < 3:
        prompt('Choose one: "r" for Rock, "p" for Paper, "s" for Scissors, "sp" for Spock, "l" for Lizard.')
        choice = shorthand_translate(input())
    
        while choice not in VALID_CHOICES:
            prompt("That's not a valid choice.")
            choice = shorthand_translate(input())

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f"You chose {choice}, computer chose {computer_choice}.")

        winner = display_winner(choice, computer_choice)

        if winner == "player":
            prompt("You win this round!")
            player_score += 1
        elif winner == "computer":
            prompt("Computer wins this round!.")
            computer_score += 1
        else:
            prompt("It's a tie! Let's try that again.")
        
        prompt(f'Current Scores: Player - {player_score}, Computer - {computer_score}')
    
    if player_score == 3:
        prompt(f"You're the ULTIMATE WINNER!")
    else:
        prompt(f"Computer is the ULTIMATE WINNER!")

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    # For invalid inputs
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()
    
    if answer[0] == 'n':
        break