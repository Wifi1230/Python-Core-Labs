from card_validator import card_valid
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    while True:
        amount = float(input("Enter an amount to be deposited: "))
        print("*********************")
        if amount < 0:
            print("That's not a valid amount")
            continue
        else:
            print(f"You deposited ${amount:.2f}")
            return amount

def withdraw(balance):
    while True:
        amount = float(input("Enter amount to be withdrawn: "))
        print("*********************")
        if amount > balance:
            print("Insufficient funds")
            continue
        elif amount < 0:
            print("Amount must be greater than 0")
            continue
        else:
            print(f"You withdrawn ${amount:.2f}")
            return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("*********************")
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
            show_balance(balance)
        elif choice == '3':
            balance -= withdraw(balance)
            show_balance(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

if __name__ == '__main__':
    while not card_valid():
        print("Your card is invalid. Please try again.")
        print("*********************")
    main()
