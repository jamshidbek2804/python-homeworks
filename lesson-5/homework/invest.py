def invest(amount, rate, years):
    i = 1
    while (i <= years):
        amount += amount*rate
        print(f"year {i}: ${amount: .2f}")
        i += 1

def main():
    depozit = float(input("Enter the initial amount: "))
    foiz = float(input("Enter the annual interest rate (as a decimal): "))
    yil = int(input("Enter the number of years: "))
    invest(depozit, foiz, yil)
if __name__=="__main__":
    main()
