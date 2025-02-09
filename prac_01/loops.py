def main_1():
    for i in range(1,21,2):
        print(i,end=' ')
    print()

def main_a():
    for i in range(1,100 + 1,10):
        print(i,end=' ')
    print()

def main_b():
    for i in range (20,0,-1):
        print(i,end=' ')
    print()

def main_c():
    stars = int(input("Enter number of stars: "))
    while stars <=0:
        print("invalid input")
        stars = int(input("Enter number of stars: "))
    for i in range(1,stars+1):
        print("*",end='')
    print()

def main_d():
    stars = int(input("Enter number of stars: "))
    while stars <= 0:
        print("invalid input")
        stars = int(input("Enter number of stars: "))
    for i in range(1, stars + 1):
        print(i*"*", end='\n')
    print()

main_1()
main_a()
main_b()
main_c()
main_d()