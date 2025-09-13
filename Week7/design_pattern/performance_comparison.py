import time
from services import UserService, OrderService
from services_singleton import UserServiceSingleton, OrderServiceSingleton
from db_singleton import db

def test_normal_mode():
    """Test normal mode (no singleton)"""
    print("Testing NORMAL mode (no singleton)...")
    
    start_time = time.time()
    
    # Create service instances
    user_service = UserService()
    order_service = OrderService()
    
    # Execute 100 operations
    for i in range(100):
        user_service.get_user(1)
        order_service.get_orders(1)
    
    end_time = time.time()
    runtime_ms = (end_time - start_time) * 1000
    print(f"Normal mode: {runtime_ms:.2f} ms")
    return runtime_ms

def test_singleton_mode():
    """Test singleton mode (with connection reuse)"""
    print("Testing SINGLETON mode (with connection reuse)...")
    
    start_time = time.time()
    
    # Create service instances
    user_service = UserServiceSingleton()
    order_service = OrderServiceSingleton()
    
    # Execute 100 operations
    for i in range(100):
        user_service.get_user(1)
        order_service.get_orders(1)
    
    # Close connection at the end
    db.close_connection()
    
    end_time = time.time()
    runtime_ms = (end_time - start_time) * 1000
    print(f"Singleton mode: {runtime_ms:.2f} ms")
    return runtime_ms

def main():
    print("="*70)
    print("PERFORMANCE COMPARISON: NORMAL vs SINGLETON")
    print("="*70)
    
    # Test normal mode
    normal_time = test_normal_mode()
    print()
    
    # Test singleton mode
    singleton_time = test_singleton_mode()
    
    print()
    print("="*70)
    print("RESULTS:")
    print(f"Normal mode:    {normal_time:.2f} ms")
    print(f"Singleton mode: {singleton_time:.2f} ms")
    
    print()
    print("ANALYSIS:")
    if singleton_time < normal_time:
        improvement = ((normal_time - singleton_time) / normal_time) * 100
        print(f"✅ Singleton is {improvement:.1f}% faster than normal!")
    else:
        overhead = ((singleton_time - normal_time) / normal_time) * 100
        print(f"❌ Singleton has {overhead:.1f}% overhead")
    
    print("="*70)

if __name__ == "__main__":
    main()