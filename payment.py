class Payment:
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        return "Paying", amount, "using credit card"

class UPIPayment(Payment):
    def make_payment(self, amount):
        return "Paying",amount, "using UPI"

class BankTransferPayment(Payment):
    def make_payment(self, amount):
        return "Paying",amount, "using bank transfer"

def process_payment(payment, amount):
    print(payment.make_payment(amount))

credit_card_payment = CreditCardPayment()
UPIPayment = UPIPayment()
bank_transfer_payment = BankTransferPayment()

process_payment(credit_card_payment, 50)
# Output will be: Paying 50 using credit card
process_payment(UPIpayment, 20)
# Output will be: Paying 20 using PayPal
process_payment(bank_transfer_payment, 30)
# Output willbe: Paying 30 using bank transfer
