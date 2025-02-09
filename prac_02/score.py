import random

def main():
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print(result)
    random_score = random.randint(1,100)
    random_result = calculate_result(random_score)
    print(f"Random score: {random_score}")
    print(random_result)

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