def showbalance(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit(balance):
    depositAmt = float(input("Enter the deposit amount : "))

    if depositAmt < 0:
        print(" invalid amount enter a positive amount ")

    else:
        balance += depositAmt
        print(f"you have sucessfully deposited $ {depositAmt:.2f}")

    return balance


def widrawbalance(balance):
    widrawAmt = float(input("Enter a widraw amount: "))

    if widrawAmt > balance:
        print(" insuficent balance ")


    elif widrawAmt < 0:

        print("invalid amount.Please enter a positive amount ")


    else:
        balance -= widrawAmt
        print(f"your widraw Amount is {widrawAmt:.2f}")

    return balance


def main():
    balance = 0
    isrunning = True
    while (isrunning):
        print("Banking program")
        print("1.Show Balance")
        print("2.Deposit balance")
        print("3.widrawbalance")
        print("4.exit")
        choice = input("Enter your choice 1-4: ")

        if choice == "1":
            showbalance(balance)

        elif choice == "2":
           balance = deposit(balance)

        elif choice == "3":
            balance = widrawbalance(balance)
        elif choice == "4":
            isrunning = False

        else:

            print(" not a valid choice ! ")


if __name__ == "__main__":
    main()



