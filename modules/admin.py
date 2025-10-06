def view_all_accounts(customers):
    print("\n===== All Customer Accounts =====")
    for c in customers:
        print(f"ID: {c['id']} | Name: {c['name']} | Balance: ₹{c['balance']}")
    print("=================================")


def view_loan_requests(loan_requests, customers):
    print("\n===== Loan Requests =====")
    if not loan_requests:
        print("No loan requests found.")
    else:
        for req in loan_requests:
            customer = next((c for c in customers if c["id"] == req["customer_id"]), None)
            if customer:
                print(f"Customer: {customer['name']} | Amount: ₹{req['amount']} | Status: {req['status']}")
    print("===========================")


def approve_loan(loan_requests, customer_id):
    for req in loan_requests:
        if req["customer_id"] == customer_id and req["status"] == "Pending":
            req["status"] = "Approved"
            print(" Loan approved successfully.")
            return
    print(" No pending loan request found for this customer.")


def reject_loan(loan_requests, customer_id):
    for req in loan_requests:
        if req["customer_id"] == customer_id and req["status"] == "Pending":
            req["status"] = "Rejected"
            print(" Loan rejected successfully.")
            return
    print(" No pending loan request found for this customer.")
