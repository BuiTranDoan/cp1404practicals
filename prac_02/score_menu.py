def main():
    MENU = """\n(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
    score = get_valid_score("Enter your score: ")
    print(MENU)
    choice = get_choice(">>> ")
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter your score: ")
        elif choice == "P":
            result = calculate_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        print(MENU)
        choice = get_choice(">>> ")
    print("That's it for today, see you again :)")


def show_stars(score):
    scores = int(score)
    for i in range (0,scores):
        print("*",end="")


def get_choice(prompt):
    choices = ["G","P","S","Q"]
    enter_choice = input(prompt).upper()
    while enter_choice not in choices:
        print("Invalid choice")
        enter_choice = input(prompt).upper()
    return enter_choice

def get_valid_score(prompt):
    enter_score = float(input(prompt))
    while enter_score < 0 or enter_score > 100:
        print("Invalid score! Enter again")
        enter_score = float(input(prompt))
    return enter_score

def calculate_result(prompt):
    if prompt < 0 or prompt > 100:
        return "Invalid score"
    elif prompt >= 50:
        if prompt >= 90:
            return "Excellent"
        else:
            return "Passable"
    else:
        return "Bad"

main()