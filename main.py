from data.customers_data import customers, loan_requests
from modules import admin, customer

def admin_menu():
    while True:
        print("\n===== Admin Menu =====")
        print("1. View All Accounts")
        print("2. View Loan Requests")
        print("3. Approve Loan")
        print("4. Reject Loan")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin.view_all_accounts(customers)
        elif choice == "2":
            admin.view_loan_requests(loan_requests, customers)
        elif choice == "3":
            cid = int(input("Enter Customer ID to approve loan: "))
            admin.approve_loan(loan_requests, cid)
        elif choice == "4":
            cid = int(input("Enter Customer ID to reject loan: "))
            admin.reject_loan(loan_requests, cid)
        elif choice == "5":
            break
        else:
            print("⚠️ Invalid choice.")

def customer_menu():
    while True:
        print("\n===== Customer Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Money")
        print("5. Apply for Loan")
        print("6. View Loan Status")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            pin = int(input("Enter PIN: "))
            customer.check_balance(customers, name, pin)
        elif choice == "2":
            name = input("Enter name: ")
            pin = int(input("Enter PIN: "))
            amt = float(input("Enter amount: "))
            customer.deposit(customers, name, pin, amt)
        elif choice == "3":
            name = input("Enter name: ")
            pin = int(input("Enter PIN: "))
            amt = float(input("Enter amount: "))
            customer.withdraw(customers, name, pin, amt)
        elif choice == "4":
            name = input("Enter your name: ")
            pin = int(input("Enter PIN: "))
            receiver = input("Enter receiver name: ")
            amt = float(input("Enter amount to transfer: "))
            customer.transfer_money(customers, name, pin, receiver, amt)
        elif choice == "5":
            name = input("Enter name: ")
            amt = float(input("Enter loan amount: "))
            customer.apply_loan(loan_requests, customers, name, amt)
        elif choice == "6":
            name = input("Enter name: ")
            customer.view_loan_status(loan_requests, customers, name)
        elif choice == "7":
            break
        else:
            print("⚠️ Invalid choice.")

def main():
    print("===== Welcome to Python Bank Management System =====")
    while True:
        print("\n1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            print("Thank you for using the Bank Management System! Have a Great Day !")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
