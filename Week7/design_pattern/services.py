import sqlite3

# Class for user operations (Normal mode - no singleton)
class UserService:
    def get_user(self, user_id):
        # Connect to database directly
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        
        # Search user by ID
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        
        # Close connection and return result
        conn.close()
        return result

# Class for order operations (Normal mode - no singleton)
class OrderService:
    def get_orders(self, user_id):
        # Connect to database directly
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        
        # Search all orders of user
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        
        # Close connection and return result
        conn.close()
        return result