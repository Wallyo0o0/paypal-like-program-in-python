def showbalance():
    print(f"Your Balance is {balance:.2f}$")
def deposit():
    amount = float(input("Enter an amount to be deposited"))
    if amount > balance:
        print("Insufficient amount")
        return 0
    elif amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount
def withdraw():
    amount = float(input("Enter an amount you want to withdraw"))
    if amount < 0:
        print("That was an invalid amount")
        return 0
    else:
        return amount
balance = 0
is_running = True 

while is_running:
    print("---WELCOME TO THIS BANKING PROGRAM---")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice = input("Choose your option with 1,2,3,4: ")

    if choice == "1":
        showbalance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
         is_running = False
    else:
        print("That was and invalid choice")

print("Thanks for testing this program have a nice day!")