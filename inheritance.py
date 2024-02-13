class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount}KES send to {receipient} successful")
        else:
            print("you have insufficient funds to complete this transfer,")


class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, idno):
        super(). __init__ (account_balance, phone_number)
        self.idno = idno

    def buyairtime(self, amount):
        self.account_balance -= amount
        print(f"{amount}KES airtime bought successful")


class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, business_id):
        super().__init__(account_balance, business_id)
        self.business_id = business_id

    def receive_payment(self, amount):
        self.account_balance += amount
        print(f"{amount}KES received from customer")


personal = PersonalMpesa(2000, 908989890, 445678)
personal.send_money(300, 32090999)
personal.buyairtime(150)

personal=BusinessMpesa(7000,345678)
personal.receive_payment(4500)