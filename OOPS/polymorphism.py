"""Definition: Same method name, different behaviors (many forms).

Real-World Analogy: A "pay" button on different apps — works differently for Spotify (music), Netflix (movies), Uber (ride)."""

class PaymentGateway:
    def pay(self, amount):
        pass

class PayPal(PaymentGateway):
    def pay(self, amount):
        return f"Processing PayPal payment of ${amount}"

class Stripe(PaymentGateway):
    def pay(self, amount):
        return f"Processing Stripe payment of ${amount}"


class Bitcoin(PaymentGateway):
    def pay(self, amount):
        return f"Processing Bitcoin payment of ${amount}"


for gateway in [PayPal(), Stripe(), Bitcoin()]:
    print(gateway.pay(100))