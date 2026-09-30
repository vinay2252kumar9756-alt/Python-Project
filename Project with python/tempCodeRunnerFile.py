import random
from datetime import datetime


class ATMSystem:
    def __init__(self):
        self.accounts = {}

    def generate_account_number(self):
        while True:
            acc_number = str(random.randint(100000000000, 999999999999))
            if acc_number not in self.accounts:
                return acc_number

    def create_account(self, name, acc_type, pin, balance, dob,
                       branch_name, branch_address, ifsc_code):

        acc_number = self.generate_account_number()

        self.accounts[acc_number] = {
            "name": name,
            "dob": dob,
            "type": acc_type,
            "pin": pin,
            "balance": balance,
            "branch_name": branch_name,
            "branch_address": branch_address,
            "ifsc_code": ifsc_code,
            "transactions": []
        }

        print("\n✅ Account Created Successfully!")
        print(f"Your Account Number: {acc_number}\n")

    def login(self, acc_number):
        if acc_number not in self.accounts:
            print("❌ Account not found!\n")
            return None

        attempts = 3
        while attempts > 0:
            pin = input("Enter PIN: ").strip()   # ✅ FIXED

            if pin == self.accounts[acc_number]["pin"]:
                print(f"\n✅ Welcome {self.accounts[acc_number]['name']}!\n")
                return acc_number
            else:
                attempts -= 1
                print(f"❌ Wrong PIN! Attempts left: {attempts}")

        print("❌ Too many failed attempts!\n")
        return None

    def account_details(self, acc_number):
        user = self.accounts[acc_number]
        print("\n===== ACCOUNT DETAILS =====")
        print(f"Name: {user['name']}")
        print(f"DOB: {user['dob']}")
        print(f"Account Type: {user['type']}")
        print(f"Balance: ₹{user['balance']:.2f}")
        print(f"Branch Name: {user['branch_name']}")
        print(f"Branch Address: {user['branch_address']}")
        print(f"IFSC Code: {user['ifsc_code']}")
        print("===========================\n")

    def check_balance(self, acc_number):
        print(f"💰 Balance: ₹{self.accounts[acc_number]['balance']:.2f}\n")

    def deposit(self, acc_number):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("❌ Invalid amount!\n")
                return

            self.accounts[acc_number]['balance'] += amount

            self.accounts[acc_number]['transactions'].append(
                f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - Deposited ₹{amount}"
            )

            print("✅ Deposit successful!")
            print(f"Total Balance: ₹{self.accounts[acc_number]['balance']:.2f}\n")

        except:
            print("❌ Invalid input!\n")

    def withdraw(self, acc_number):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("❌ Invalid amount!\n")
            else:
                self.accounts[acc_number]['balance'] -= amount

                self.accounts[acc_number]['transactions'].append(
                    f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - Withdrawn ₹{amount}"
                )

                print("✅ Withdrawal successful!")
                print(f"Remaining Balance: ₹{self.accounts[acc_number]['balance']:.2f}\n")

        except:
            print("❌ Invalid input!\n")

    def mini_statement(self, acc_number):
        print("\n--- Mini Statement (Last 5) ---")
        transactions = self.accounts[acc_number]['transactions']
        if not transactions:
            print("No transactions yet.")
        else:
            for t in transactions[-5:]:
                print(t)
        print("-------------------------------\n")

    def menu(self, acc_number):
        while True:
            print("====== ATM MENU ======")
            print("1. Account Details")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Mini Statement")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.account_details(acc_number)
            elif choice == "2":
                self.check_balance(acc_number)
            elif choice == "3":
                self.deposit(acc_number)
            elif choice == "4":
                self.withdraw(acc_number)
            elif choice == "5":
                self.mini_statement(acc_number)
            elif choice == "6":
                print("✅ Logged out successfully!\n")
                break
            else:
                print("❌ Invalid choice!\n")


# ===== MAIN PROGRAM =====

atm = ATMSystem()

while True:
    print("====== ATM SYSTEM ======")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        acc_type = input("Enter account type: ")

        while True:
            pin = input("Set 4-digit PIN: ").strip()   # ✅ FIXED
            if pin.isdigit() and len(pin) == 4:
                break
            else:
                print("❌ PIN must be exactly 4 digits!\n")

        try:
            balance = float(input("Enter initial balance: "))
        except:
            print("❌ Invalid balance! Setting to 0.")
            balance = 0.0

        dob = input("Enter DOB: ")
        branch_name = input("Branch name: ")
        branch_address = input("Branch address: ")
        ifsc = input("IFSC code: ")

        atm.create_account(name, acc_type, pin, balance, dob,
                           branch_name, branch_address, ifsc)

    elif choice == "2":
        acc_number = input("Enter account number: ").strip()

        user = atm.login(acc_number)
        if user:
            atm.menu(user)

    elif choice == "3":
        print("🙏 Thank you for using ATM!\n")
        break

    else:
        print("❌ Invalid choice!\n")