# Normal approach without Factory pattern
class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}...")
        return True

class StripePayment:
    def process_payment(self, amount):
        print(f"Processing Stripe payment of ${amount}...")
        return True

class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}...")
        return True

# Normal checkout function without factory
def checkout_normal(payment_method, amount):
    # Direct instantiation based on payment method
    if payment_method == "paypal":
        processor = PayPalPayment()
    elif payment_method == "stripe":
        processor = StripePayment()
    elif payment_method == "credit_card":
        processor = CreditCardPayment()
    else:
        raise ValueError(f"Invalid payment method: {payment_method}")
    
    return processor.process_payment(amount)