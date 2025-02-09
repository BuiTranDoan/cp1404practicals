
MINIMUM = 8
def main():
    password = get_password()
    while len(password) < MINIMUM:
        print("A password must be at least 8 characters")
        password = input("Password: ")
    for i in range(0,len(password)):
        print("*",end="")

def get_password():
    password = input("Password: ")
    return password
main()