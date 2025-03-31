# Atm_Simulation_Project
Overview:
This Python-based ATM Management System interacts with a MySQL database to manage banking functionalities such as user authentication, balance inquiry, cash withdrawal, cash deposit, transaction history, and admin management.
Features & Functionalities:
**1. Database Setup & Table Creation**
The system connects to a MySQL database (Atm_Machine) and creates four main tables:
admins: Stores admin credentials for managing the ATM system.
customers: Stores customer details like name, email, phone, and address.
accounts: Stores account information, including account numbers, PINs, and balance.
transactions: Records transaction history (deposits and withdrawals).
**2. Admin Login**
Admins can log in using a username and password.
If the credentials match the admins table, access is granted.
If authentication fails, an "Invalid Credentials" message is shown
**3. Customer Authentication**
Customers authenticate using account number and PIN.
If the credentials match the accounts table, access is granted.
If authentication fails, an "Invalid Credentials" message is displayed.
**4. ATM Functionalities for Customers**
Once logged in, a customer can access the ATM Menu with the following options:
1) Balance Inquiry
The system retrieves the current balance from the database and displays it.
2) Cash Withdrawal
The user enters the amount to withdraw.
If the amount is greater than or equal to ₹1000, it checks if the user has sufficient balance.
If sufficient balance is available:
The amount is deducted.
The new balance is updated in the database.
A transaction record is inserted into the transactions table.
If insufficient funds are available, an error message is displayed.
3) Cash Deposit
The user enters the amount to deposit.
The balance is updated in the database.
A record is inserted into the transactions table.
The system displays the new balance.
4) Transaction History
The system retrieves the last 5 transactions from the transactions table.
Each transaction displays:
Transaction Type (Deposit/Withdrawal)
Amount
Date & Time
**5) Exit**
The user can choose to exit the system.
5. Admin & Customer Menu
The program starts with a Main Menu, where users can:
Admin Login
Customer Login
Exit the program
If the admin logs in, they can manage ATM functionalities.
If a customer logs in, they can perform transactions.
The program runs in a loop until the user exits.

