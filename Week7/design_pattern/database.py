import sqlite3

# Function to create tables
def create_tables():
    # Connect to database
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Save changes and close connection
    conn.commit()
    conn.close()
    print("Tables created successfully!")

# Function to insert sample data
def insert_sample_data():
    # Connect to database
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    # Users data
    users_data = [
        (1, 'Alice Johnson', 'alice@example.com'),
        (2, 'Bob Smith', 'bob@example.com'),
        (3, 'Carol Davis', 'carol@example.com')
    ]
    
    # Insert users
    cursor.executemany('''
        INSERT OR REPLACE INTO users (id, name, email) VALUES (?, ?, ?)
    ''', users_data)
    
    # Orders data
    orders_data = [
        (1, 1, 'Laptop', 999.99),
        (2, 1, 'Mouse', 29.99),
        (3, 2, 'Keyboard', 79.99),
        (4, 2, 'Monitor', 299.99),
        (5, 3, 'Headphones', 149.99),
        (6, 3, 'Webcam', 89.99),
        (7, 3, 'Microphone', 199.99)
    ]
    
    # Insert orders
    cursor.executemany('''
        INSERT OR REPLACE INTO orders (id, user_id, product_name, amount) VALUES (?, ?, ?, ?)
    ''', orders_data)
    
    # Save changes and close connection
    conn.commit()
    conn.close()
    print("Sample data inserted successfully!")

# Main function to create 
def create_database():
    create_tables()
    insert_sample_data()
    print("Database created successfully!")
