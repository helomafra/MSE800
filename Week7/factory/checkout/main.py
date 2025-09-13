from chackout_factory import checkout

def main():
    print("Starting Factory Pattern Demonstration...")
    print()
    
    print("="*50)
    print("FACTORY PATTERN DEMO - PAYMENT PROCESSING")
    print("="*50)
    
    # Test different payment methods
    payments = [
        ("paypal", 100.50),
        ("stripe", 250.75),
        ("credit_card", 75.25)
    ]
    
    print("\nProcessing payments:")
    print("-" * 30)
    
    for method, amount in payments:
        print(f"\nProcessing ${amount} with {method.upper()}:")
        result = checkout(method, amount)
        if result:
            print("✅ Payment successful!")
        else:
            print("❌ Payment failed!")
    
if __name__ == "__main__":
    main()