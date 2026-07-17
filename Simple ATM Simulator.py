# Simple ATM Simulator

PIN = "1234"
balance = 5000

def check_balance():
    print("Current Balance: ₹", balance)

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("Amount Deposited Successfully.")

def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
    else:
        print("Insufficient Balance.")

entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin == PIN:

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid Choice")

else:
    print("Incorrect PIN.")