
def prompt(message):
    print(f"==> {message}")

def display_winner(choice, computer_choice):
    if ((choice == "rock" and computer_choice == "scissors") or 
        (choice == "paper" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "paper")or
        (choice == "lizard" and computer_choice == "spock") or
        (choice == "spock" and computer_choice == "scissors") or
        (choice == "scissors" and computer_choice == "lizard") or
        (choice == "lizard" and computer_choice == "paper") or
        (choice == "paper" and computer_choice == "spock") or
        (choice == "spock" and computer_choice == "rock")):
        return "player"
    elif ((choice == "rock" and computer_choice == "paper") or
        (choice == "paper" and computer_choice == "scissors") or
        (choice == "scissors" and computer_choice == "rock") or
        (choice == "spock" and computer_choice == "lizard") or
        (choice == "scissors" and computer_choice == "spock") or
        (choice == "lizard" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "lizard") or
        (choice == "spock" and computer_choice == "paper") or
        (choice == "rock" and computer_choice == "spock")):
        return "computer"
    else:
        return "tie"


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
