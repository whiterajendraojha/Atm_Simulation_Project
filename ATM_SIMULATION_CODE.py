import mysql.connector
# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9668263729",
    database="Atm_Machine"
    )
cursor = conn.cursor()
# Admin Login Function
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    cursor.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (username, password))
    admin = cursor.fetchone()
    return admin is not None
# User Authentication Function
def authenticate_user():
    account_number=input("Enter account number:")
    pin=int(input("Enter PIN:"))
    cursor.execute("SELECT * FROM accounts WHERE account_number=%s AND pin_code=%s", (account_number, pin))
    account = cursor.fetchone()
    return account
# Balance Inquiry
def balance_inquiry(account_id):
    cursor.execute("SELECT balance FROM accounts WHERE account_id=%s", (account_id,))
    balance = cursor.fetchone()
    if balance:
        print(f"\nCurrent Balance: {balance[0]:,.2f}")
    else:
        print("Account not found.")
# Cash Withdrawal
def withdraw_cash(account_id):
    amount=float(input("Enter amount to withdraw:"))
    if (amount>=1000):
        cursor.execute("SELECT balance FROM accounts WHERE account_id=%s", (account_id,))
        balance = cursor.fetchone()[0]

        if amount > balance:
            print("Insufficient funds.")
        else:
            new_balance = balance - amount
            cursor.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (new_balance, account_id))
            conn.commit()
            cursor.execute("INSERT INTO transactions (account_id, transaction_type, amount) VALUES (%s, 'withdrawal', %s)",
                        (account_id, amount))
            conn.commit()
            print(f"Rs.{amount:,.2f} withdrawn successfully.")
            print(f"New Balance is Rs.{new_balance:,.2f}.")
    else:
        print(f"Insufficient Found In Your Account:")

# Cash Deposit
def deposit_cash(account_id):
    amount=float(input("Enter amount to deposit:"))
    cursor.execute("SELECT balance FROM accounts WHERE account_id=%s", (account_id,))
    balance = cursor.fetchone()[0]
    new_balance = balance + amount
    cursor.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (new_balance, account_id))
    conn.commit()
    cursor.execute("INSERT INTO transactions (account_id, transaction_type, amount) VALUES (%s, 'deposit', %s)",
                   (account_id, amount))
    conn.commit()
    print(f"Rs.{amount:,.2f} deposited successfully.")
    print(f" New balance is Rs.{new_balance:,.2f}.")

#Transaction History
def transaction_history(account_id):
    cursor.execute(
        "SELECT transaction_type, amount, transaction_date FROM transactions WHERE account_id=%s ORDER BY transaction_date DESC LIMIT 5",
        (account_id,))
    transactions = cursor.fetchall()
    if transactions:
        print("Recent Transactions:")
        for transaction in transactions:
            print(f"{transaction[2]} - {transaction[0].capitalize()} - Rs.{transaction[1]:,.2f}")
    else:
        print("No transactions found.")
# Main ATM Menu
def atm_menu(account_id):
    while True:
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            balance_inquiry(account_id)
        elif choice == "2":
            withdraw_cash(account_id)
        elif choice == "3":
            deposit_cash(account_id)
        elif choice == "4":
            transaction_history(account_id)
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


#Main Program
while(True):
    print("Choose:\n1) Admin Login\n2) Customer Login\n3) Exit")
    Option = int(input("Your Choice: "))
    if Option == 1:
        if admin_login():
            print("Admin login successfully.")
        else:
            print("Invalid Credentials")
    elif Option == 2:
        account = authenticate_user()
        if account:
            print("User authenticated successfully.")
            atm_menu(account[0])
        else:
            print("Invalid Credentials")
    elif Option == 3:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option, please try again.")




# Close the connection
cursor.close()
conn.close()
