import mysql.connector

# Connect to MySQL (root credentials)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Atm_Machine"
)
cursor = conn.cursor()


# Create Database and Tables

# cursor.execute("CREATE DATABASE  Atm_Machine")
# cursor.execute("USE Atm_Machine")

    # Create Admin table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        admin_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL
    )
    """)

    # Create Customers table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE,
        phone VARCHAR(15),
        address VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create Accounts table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        account_number VARCHAR(20) UNIQUE NOT NULL,
        pin_code CHAR(4) NOT NULL,
        balance FLOAT(15, 2) DEFAULT 0.00,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
    )
    """)

    # Create Transactions table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INT AUTO_INCREMENT PRIMARY KEY,
        account_id INT,
        transaction_type ENUM('deposit', 'withdrawal') NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
    )
    """)

    # Insert sample data
cursor.execute("INSERT IGNORE INTO admins (admin_id,username, password) VALUES ('1','nitpbank', 'nitp1234')")
cursor.execute(
        "INSERT IGNORE INTO customers ( customer_id,name, email, phone, address) VALUES ('1000','Rohit Sharma', 'rohitsharma1@gmail.com', '9833224150', '264,Azad Nagar,Andheri West, Mumbai'),('1001','Vivek Sharma','viveksharma2@gmail.com','7712388082','63,Chandralok Colony,Khajrana,Indore'),(1002,'Jagarnath raj','jagarnath2002@gmail.com',9685741256,'65,bhubaneswar,odisha'),(1003,'durgacharan','durgacharan200@gmail.com','9685263419','58,puri,odisha'),('1004','Amit Mishra','amitmishra@gmail.com','8822112300','21,Raj Nagar,Indore')")


cursor.execute(
        "INSERT IGNORE INTO accounts (customer_id, account_number, pin_code, balance) VALUES ('1000', '123100002314', '2233', 00.00),('1001','123100002354','3322','100.00'),('1002','123100002365','3344','1000.00'),('1003','123100002376','3388','200.00'),('1004','123100002325','1234','120.00')")
conn.commit()


cursor.close()
conn.close()

