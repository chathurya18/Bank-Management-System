from modules.utils import authenticate

def check_balance(customers, name, pin):
    user = authenticate(customers, name, pin)
    if user:
        print(f"\n Current Balance for {user['name']}: ₹{user['balance']}")
    else:
        print(" Invalid name or PIN.")


def deposit(customers, name, pin, amount):
    user = authenticate(customers, name, pin)
    if user and amount > 0:
        user["balance"] += amount
        print(f" ₹{amount} deposited successfully. New Balance: ₹{user['balance']}")
    else:
        print(" Invalid credentials or amount.")


def withdraw(customers, name, pin, amount):
    user = authenticate(customers, name, pin)
    if user and amount > 0 and amount <= user["balance"]:
        user["balance"] -= amount
        print(f" ₹{amount} withdrawn successfully. Remaining Balance: ₹{user['balance']}")
    else:
        print(" Invalid credentials or insufficient balance.")


def transfer_money(customers, name, pin, receiver_name, amount):
    sender = authenticate(customers, name, pin)
    receiver = next((c for c in customers if c["name"].lower() == receiver_name.lower()), None)
    
    if sender and receiver and sender != receiver and amount > 0 and sender["balance"] >= amount:
        sender["balance"] -= amount
        receiver["balance"] += amount
        print(f" ₹{amount} transferred from {sender['name']} to {receiver['name']}.")
    else:
        print(" Transaction failed. Check details.")


def apply_loan(loan_requests, customers, name, amount):
    user = next((c for c in customers if c["name"].lower() == name.lower()), None)
    if user:
        loan_requests.append({"customer_id": user["id"], "amount": amount, "status": "Pending"})
        print(f" Loan request for ₹{amount} submitted successfully.")
    else:
        print(" Customer not found.")


def view_loan_status(loan_requests, customers, name):
    user = next((c for c in customers if c["name"].lower() == name.lower()), None)
    if user:
        found = False
        print(f"\n===== Loan Status for {user['name']} =====")
        for req in loan_requests:
            if req["customer_id"] == user["id"]:
                print(f"Amount: ₹{req['amount']} | Status: {req['status']}")
                found = True
        if not found:
            print("No loan requests found.")
        print("==========================================")
    else:
        print("Customer not found.")
