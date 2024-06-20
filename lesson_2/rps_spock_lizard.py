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
# - how to resolve?).
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

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    if ((choice == "rock" and computer_choice == "scissors") or 
        (choice == "paper" and computer_choice == "rocks") or
        (choice == "scissors" and computer_choice == "paper")or
        (choice == "lizard" and computer_choice == "spock") or
        (choice == "spock" and computer_choice == "scissors") or
        (choice == "scissors" and computer_choice == "lizard") or
        (choice == "lizard" and computer_choice == "paper") or
        (choice == "paper" and computer_choice == "spock") or
        (choice == "spock" and computer_choice == "rock")):
        prompt("You win!")
    elif ((choice == "rock" and computer_choice == "paper") or
        (choice == "paper" and computer_choice == "scissors") or
        (choice == "scissors" and computer_choice == "rock") or
        (choice == "spock" and computer_choice == "lizard") or
        (choice == "scissors" and computer_choice == "spock") or
        (choice == "lizard" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "lizard") or
        (choice == "spock" and computer_choice == "paper") or
        (choice == "rock" and computer_choice == "spock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def shorthand_translate(shorthand):
    match shorthand:
        case "r":
            return "rock"
        case "p":
            return "paper"
        case "s":
            return "scissors"
        case "sp":
            return "spock"
        case "l":
            return "lizard"


while True: 
    prompt(f'Choose one: "r" for Rock, "p" for Paper, "s" for Scissors, "sp" for Spock, "l" for Lizard.')
    choice = shorthand_translate(input())
    
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = shorthand_translate(input())

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}, computer chose {computer_choice}.")

    display_winner(choice, computer_choice)
    
    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()
    
    if answer[0] == 'n':
        break