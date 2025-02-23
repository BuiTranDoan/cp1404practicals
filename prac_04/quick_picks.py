import random

NUMBERS_MIN = 1
NUMBERS_MAX = 45
NUMBERS_PER_PICK = 6
def main():
    num_picks = int(input("How many quick picks? "))
    for i in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))
def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(NUMBERS_MIN, NUMBERS_MAX)
        if num not in numbers:  # Ensure no duplicates
            numbers.append(num)
    numbers.sort()  # Sort the numbers in ascending order
    return numbers

main()