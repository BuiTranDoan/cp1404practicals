DISCOUNT = 100
TOTAL= 0
items = int(input("Enter number of items: "))
while items <0:
    print("invalid input")
    items = int(input("Enter number of items: "))
for i in range(0,items):
    price = float(input("Price of item: "))
    TOTAL += price
if TOTAL> DISCOUNT:
    TOTAL -= TOTAL*10/100
print(f"Total price of {items} item is ${TOTAL:.2f}")
