"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

menu = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Please enter your name: ").title()
print(menu)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice!")
    print(menu)
    choice = input(">>>").upper()
print("Finished.")