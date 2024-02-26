"""
Welcome to ATM machine reverse engineering:
This is just a simple demo project without database system.
I will implement database functionality to login our account,
in my next commit.
                                                        -vizon
"""
class Account:
    account_counter = 0
    wrong_count = 3

    def __init__(self, account_name, nid_num, password):
        self.account_name = account_name
        self.nid_num = nid_num
        self.password = password
        self.account_number = self.account_num_generator()
        self.balance = 0.0
        Account.account_counter += 1

    def __str__(self):
        print(f"Hi, {self.account_name}, Your account created successfully.")
        print(f"Your account number is {self.account_number}")
        print(f"Your current balance is: {self.balance} ")
        print("Thank You For Choosing Us.")

    def account_num_generator(self):
        self.account_counter += 1
        return "100" + str(self.nid_num) + f"0{str(self.account_counter)}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            print(
                f"Transferred ${amount} to {recipient}. Your new balance: ${self.balance}"
            )
        else:
            print("Invalid transfer amount or insufficient funds.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def change_password(self):
        while self.wrong_count >= 0:
            p_matched, m_pass = self.is_password_matched()
            if p_matched:
                new_password = input("Enter your new password: ")
                self.password = new_password
                print("Your password updated successfully.")
                break

            else:
                self.wrong_count -= 1
                print(f"Incorrect password! You have {self.wrong_count} try left")
                quit_ = input("Quit if you dont know your password. (Y/N): ")
                if quit_ == "Y".lower():
                    break
                elif quit_ == "N".lower():
                    if self.wrong_count <= 0:
                        print(
                            "Your account blocked! Please visit nearest bank counter."
                        )
                        break
                else:
                    print("Invalid input! Try again.")

    def is_password_matched(self):
        ex_password = input("Enter your current password: ")
        if self.password == ex_password:
            return True, ex_password
        else:
            return False, None

    def main_menu(self):
        flag = True

        while flag:
            print(
                "Select your action: "
                "1: [Deposit] "
                "2: [Withdraw] "
                "3: [Fund Transfer] "
                "4: [Balance Check] "
                "Q: [Quit]"
            )
            user_input2 = input()
            if user_input2 == "1":
                amt = float(input("How much money do you want to deposit? "))
                self.deposit(amt)

                inp = input("Press '*' for main menu and any key for quit: ")
                if inp == '*':
                    flag = True
                else:
                    break
            elif user_input2 == "2":
                amt = float(input("How much money do you want to withdraw? "))
                self.withdraw(amt)
                inp = input("Press '*' for main menu and any key for quit: ")
                if inp == '*':
                    flag = True
                else:
                    break
            elif user_input2 == "3":
                r_ac = int(input("Please enter recipient account number: "))
                amt = float(input("Enter amount to be sent: "))
                self.transfer(r_ac, amt)
                inp = input("Press '*' for main menu and any key for quit: ")
                if inp == '*':
                    flag = True
                else:
                    break
            elif user_input2 == "4":
                self.check_balance()
                inp = input("Press '*' for main menu and any key for quit: ")
                if inp == '*':
                    flag = True
                else:
                    break
            else:
                print("Thank you for using our services.")
                break

def dashboard():
    print("""----------------Welcome To XYZ Bank----------------""")
    print("Press 1 for 'Sign Up' 2 for 'Login' ")
    user_input = input()
    if user_input == str(1):
        print(
            """
            ----------------Welcome To XYZ Bank----------------
                  Your New Bank Account is Going to Be Created...
            """
        )
        name = input("Please enter your fullname: ")
        nid = input("Enter your national ID number: ")
        password = input("Enter your password: ")
        new_account = Account(name, nid, password)
        new_account.__str__()
        print()
        new_account.main_menu()
    elif user_input == "2":
        print(
            """
                ----------------Welcome To XYZ Bank----------------
                Please Enter Your Account Number and Password to Login...
            """
        )
        ac_number = input("Please enter account number: ")
        password = input("Enter your password.")

    else:
        raise "Invalid Input!"


dashboard()
