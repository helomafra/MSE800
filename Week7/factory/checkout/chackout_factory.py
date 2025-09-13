from abc import ABC, abstractmethod

# Abstract base class for payment processors
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

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
    _processors = {
        "paypal": PayPalPayment,
        "stripe": StripePayment,
        "credit_card": CreditCardPayment
    }
    
    @classmethod
    def create_payment_processor(cls, payment_method):
        processor_class = cls._processors.get(payment_method)
        if not processor_class:
            raise ValueError(f"Invalid payment method: {payment_method}")
        return processor_class()
    
    @classmethod
    def register_processor(cls, method_name, processor_class):
        cls._processors[method_name] = processor_class

# Checkout function using the factory
def checkout(payment_method, amount):
    processor = PaymentFactory.create_payment_processor(payment_method)
    return processor.process_payment(amount)