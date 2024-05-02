class WituSacco:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 1000:
            print("Minimum deposit amount is 1000.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount < 500:
            print("Minimum withdrawal amount is 500.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

def main():
    sacco = WituSacco()
    while True:
        print("\nWitu Sacco Platform")
        
        print("1. Deposit Money")
        
        print("2. Withdraw Money")
        
        print("3. Check Account Balance")
        print("Enter 'quit' to exit.")
        
        choice = input("Enter your choice: ")
        if choice == 'quit':
            break
        elif choice == '1':
            amount = int(input("Enter the amount to deposit: "))
            sacco.deposit(amount)
            
        elif choice == '2':
            amount = int(input("Enter the amount to withdraw: "))
            sacco.withdraw(amount)
            
        elif choice == '3':
            sacco.check_balance()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()