from Payment import CreditCardPayment, MobileWalletPayment


class ProcessCreditCardPayment:
    def __init__(self, amount: int):
        self.payment_method = CreditCardPayment()
        self.amount = amount

    def process_payment(self):
        self.payment_method.payment(self.amount)


class ProcessMobileValletPayment:
    def __init__(self, amount: int):
        self.payment_method = MobileWalletPayment()
        self.amount = amount

    def process_payment(self):
        self.payment_method.payment(self.amount)