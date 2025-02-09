"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MAX_BONUS=1000
def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonus = calculate_sales_bonus(sales)
        print(f"The salesperson get {bonus:.1f}$ as bonus.")
        sales = float(input("Enter sales: $"))
    print("Farewell.")
def calculate_sales_bonus(sales):
    if sales >= MAX_BONUS:
        earning = sales * 15/100
    else:
        earning = sales *10/100
    return earning
main()