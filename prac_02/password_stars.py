MINIMUM = 8
password = input("Password: ")
while len(password) < MINIMUM:
    print("A password must be at least 8 characters")
    password = input("Password: ")
for i in range(0,len(password)):
    print("*",end="")