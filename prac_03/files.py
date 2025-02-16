name = input("Enter your name: ").title()
file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
name_from_file = file.read().strip()
file.close()
print(f"Hi {name_from_file}!")


with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())

result = first_number + second_number
print(result)

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())

print(total)