from db_singleton import db

# Class for user operations (using Singleton with connection reuse)
class UserServiceSingleton:
    def get_user(self, user_id):
        # Get persistent connection from singleton
        conn = db.get_connection()
        cursor = conn.cursor()
        
        # Search user by ID
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        
        # Don't close connection - reuse it!
        return result

# Class for order operations (using Singleton with connection reuse)
class OrderServiceSingleton:
    def get_orders(self, user_id):
        # Get persistent connection from singleton
        conn = db.get_connection()
        cursor = conn.cursor()
        
        # Search all orders of user
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        
        # Don't close connection - reuse it!
        return result