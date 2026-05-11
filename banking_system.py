# Project: Automated Banking Logic
# Author: Durga Deshmukh
# Description: A terminal-based application managing deposits, withdrawals, and balance tracking.
# Skills: Input Validation, State Management, and Conditional Logic.

def show_balance(balance):
    print(f"Your balance is: ₹{balance}")

def deposit():
    amount = float(input("Enter amount to be deposited: "))
    if amount < 0:
        print("Invalid amount...")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Invalid amount...")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("*----------WELCOME----------*")
        print("-***** Banking Program *****-")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("-------------***--------------")
        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            amount = deposit()
            balance += amount
        elif choice == "3":
            amount = withdraw(balance)
            balance -= amount
        elif choice == "4":
            is_running = False
        else:
            print("Invalid option...")
    print("Thank You...")

if __name__ == '__main__':
           main() 
