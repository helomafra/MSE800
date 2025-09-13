from services import UserService, OrderService

def demonstrate_usage():
    print("\n" + "="*50)
    print("DEMONSTRATION OF DATABASE SYSTEM")
    print("="*50)
    
    # Create instances of service classes
    user_service = UserService()
    order_service = OrderService()
    
    # Test search user
    print("\n1. Searching user with ID 1:")
    user = user_service.get_user(1)
    if user:
        print(f"   User found: ID={user[0]}, Name={user[1]}, Email={user[2]}")
    else:
        print("   User not found")
    
    # Test search orders of user 1
    print("\n2. Searching orders of user ID 1:")
    orders = order_service.get_orders(1)
    if orders:
        print(f"   Found {len(orders)} orders:")
        for order in orders:
            print(f"   - Pedido {order[0]}: {order[2]} (R${order[3]})")
    else:
        print("   No orders found")
    
    # Test search orders of user 3
    print("\n3. Searching orders of user ID 3:")
    orders = order_service.get_orders(3)
    if orders:
        print(f"   Found {len(orders)} orders:")
        for order in orders:
            print(f"   - Pedido {order[0]}: {order[2]} (R${order[3]})")
    else:
        print("   No orders found")
    
    # Test search inexistent user
    print("\n4. Searching user with ID 999 (inexistent):")
    user = user_service.get_user(999)
    if user:
        print(f"   User found: {user}")
    else:
        print("   User not found")
