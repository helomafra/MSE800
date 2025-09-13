# Abstract base class for payment processors
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement process_payment method")

# Concrete payment processor implementations
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}...")
        return True

class StripePayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Stripe payment of ${amount}...")
        return True

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}...")
        return True

# Factory class for creating payment processors
class PaymentFactory:
    @staticmethod
    def create_payment_processor(payment_method):
        #create payment processor based on payment method
        if payment_method == "paypal":
            return PayPalPayment()
        elif payment_method == "stripe":
            return StripePayment()
        elif payment_method == "credit_card":
            return CreditCardPayment()
        else:
            raise ValueError(f"Invalid payment method: {payment_method}")

# Checkout function using the factory
def checkout(payment_method, amount):
    #process payment using the factory pattern
    processor = PaymentFactory.create_payment_processor(payment_method)
    return processor.process_payment(amount)