from database import create_tables, insert_sample_data
from demo import demonstrate_usage
import time

def main():
    # Start timer
    start_time = time.time()
    
    print("Starting database system (NORMAL mode)...")
    
    # Create tables
    create_tables()
    
    # Insert sample data
    insert_sample_data()
    
    print("\nExecuting demonstration...")
    demonstrate_usage()
    
    # Calculate and show execution time
    end_time = time.time()
    runtime_ms = (end_time - start_time) * 1000
    print(f"\nExecution time: {runtime_ms:.2f} ms")

if __name__ == "__main__":
    main()
