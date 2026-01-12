'''(Payment Gateway System)
A payment gateway supports multiple payment modes.
Scenario:
Interface / abstract class PaymentMethod with pay()
Implementations: CreditCard, UPI, Wallet
Requirements:
Validate payment details before processing
Apply transaction fees differently
Execute payments using interface-based polymorphism
'''
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    """Abstract base class for payment methods."""
    def __init__(self, amount):
        self.amount = amount
        
    
    @abstractmethod
    def pay(self, amount):
        pass

    @staticmethod
    def validate_payment_details(detail, detail_type='card'):
        """Generic validator usable by child classes.
        - detail_type(card_number) 'card' expects a 16-digit numeric string.
        - detail_type(upi_id) 'upi' expects a string containing '@'.
        - detail_type(wallet_id) 'wallet' expects a non-empty string.
        """
        if detail_type == 'card':
            return detail.isdigit() and len(detail) == 16
        elif detail_type == 'upi':
            return '@' in detail and len(detail) > 3
        elif detail_type == 'wallet':
            return len(detail) > 0
        return False
    
class CreditCard(PaymentMethod):
    
    def __init__(self, amount, transaction_fee, card_number):
        super().__init__(amount)
        self.transaction_fee = transaction_fee
        self.card_number = card_number
        
    def pay(self, amount):
        total_amount = amount + self.transaction_fee
        
        #Validate payment details before processing
        if PaymentMethod.validate_payment_details(self.card_number, 'card'):
            print(f"Processing credit card payment of {total_amount}")
        else:
            print("Invalid credit card details")
            
class UPI(PaymentMethod):
    
    def __init__(self, amount, transaction_fee, upi_id):
        super().__init__(amount)
        self.transaction_fee = transaction_fee
        self.upi_id = upi_id
    
    def validate_upi_id(self):
        # Placeholder for actual UPI ID validation logic
        return PaymentMethod.validate_payment_details(self.upi_id, 'upi')
    
    def pay(self, amount):
        #Validate UPI ID before processing
        total_amount = amount + self.transaction_fee
        if PaymentMethod.validate_payment_details(self.upi_id, 'upi'):
            print(f"Processing UPI payment of {total_amount} from {self.upi_id}")
        else:
            print("Invalid UPI ID")
            
class Wallet(PaymentMethod):
    
    def __init__(self, amount, transaction_fee, wallet_id):
        super().__init__(amount)
        self.transaction_fee = transaction_fee
        self.wallet_id = wallet_id
    
    def pay(self, amount):
        #Validate wallet ID before processing
        total_amount = amount + self.transaction_fee
        if PaymentMethod.validate_payment_details(self.wallet_id, 'wallet'):
            print(f"Processing wallet payment of {total_amount} from {self.wallet_id}")
        else:
            print("Invalid wallet ID")
            
    def validate_wallet_id(self):
        #Placement for actual wallet ID validation logic
        return PaymentMethod.validate_payment_details(self.wallet_id, 'wallet')
    
def main():
    
    choice = int(input("Choose payment method: \n1. Credit Card \n2. UPI \n3. Wallet: \n"))
    
    if choice == 1:
        amount = float(input("Enter amount to pay: "))
        card_number = input("Enter credit card number: ")
        transaction_fee = 2.5  
        payment_method = CreditCard(amount, transaction_fee, card_number)
        payment_method.pay(amount)
        
    elif choice == 2:
        amount = float(input("Enter amount to pay: "))
        upi_id = input("Enter UPI ID: ")
        transaction_fee = 1.0  
        payment_method = UPI(amount, transaction_fee, upi_id)
        payment_method.pay(amount)
        
    elif choice == 3:
        amount = float(input("Enter amount to pay: "))
        wallet_id = input("Enter wallet ID: ")
        transaction_fee = 1.5
        payment_method = Wallet(amount, transaction_fee, wallet_id)
        payment_method.pay(amount)
    else:
        print("Invalid choice")
        
if __name__ == "__main__":
    main()