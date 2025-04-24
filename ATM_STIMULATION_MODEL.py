class ATM:
    def __init__(self,balance=10000, pin=9876):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

# Displays the current account balance and logs the action in transaction history.
    def acc_balance(self):
        print(f"The current balance of your account is: {self.balance}.")
        self.transaction_history.append("Balance checked.")

# Deposits a valid amount into the account and updates the balance.
    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"{amount} deposited successfully.The current account balance is: {self.balance}.")
            self.transaction_history.append(f"{amount} deposited.")
        else:
            print("Invalid deposited amount.")

# Withdraws a valid amount from the account if sufficient funds are available.
    def withdrawal(self,amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f"{amount} withdrawal done successfully.The current account balance is: {self.balance}.")
            self.transaction_history.append(f"{amount} withdrawal.")
        else:
            print("Invalid withdrawal amount")

# Allows users to change their PIN if they provide the correct old PIN.
    def pin_change(self,new_pin,old_pin):
        print(f"DEBUG: Entered Old PIN -> {repr(old_pin)}")
        if old_pin == self.pin:
            self.pin == new_pin
            print("Pin changed successfully.")
            self.transaction_history.append("Pin changed.")
        else:
            print("Invalid old pin.")

# Displays the transaction history.
    def show_transaction_history(self):
        print("Transaction History....")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transaction found.")

def atm_simulation():
    pin_attempt = input("Enter your ATM Pin: ")
    atm = ATM()
    
     # User PIN authentication
    if pin_attempt != str(atm.pin):  # Convert atm.pin to a string
        print("Incorrect PIN. Access denied.")
        return
    
    while True:
        print("\n ATM MACHINE")
        print("1.Check Balance")
        print("2.Deposit Amount")
        print("3.Withdraw Amount")
        print("4.Pin Change")
        print("5.Transaction History")
        print("6.Exit")        

        choice = input("Choose an option: ")  # Get user input properly

        if choice == "1":
            atm.acc_balance()

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            atm.withdrawal(amount)

        elif choice == "4":
            old_pin = input("Enter old PIN: ").strip()
            new_pin = input("Enter new PIN: ").strip()
            atm.pin_change(old_pin , new_pin)

        elif choice == "5":
            atm.show_transaction_history()

        elif choice == "6":
            print("Thank You! for using ATM. Visit Again...")
            break

    else:
        print("Invalid choice option.")

# Run the ATM simulation
atm_simulation()