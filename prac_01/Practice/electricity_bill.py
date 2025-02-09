def main_1():
    cent = float(input("Enter cent per kWh: "))
    kWh = float(input("Enter daily use in kWh: "))
    days = int(input("Enter number of billing days: "))
    bill = (cent/100) * kWh * days
    print(f"Estimated bill: ${bill:.2f}")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
def main_2():
    tariff = int(input("Which tariff? 11 or 31: "))
    while tariff != 11 and tariff!= 31:
        print("Invalid input")
        tariff = int(input("Which tariff? 11 or 31: "))
    kWh = float(input("Enter daily use in kWh: "))
    days = int(input("Enter number of billing days: "))
    if tariff == 11:
        bill = TARIFF_11 * kWh * days
    else:
        bill = TARIFF_31 * kWh * days
    print(f"Estimated bill: ${bill:.2f}")

# main_1()
main_2()