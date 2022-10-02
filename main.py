#1
# class Bank:
#     def __init__(self):
#         self.balanc = 0
#
#     def withdraw(self, amount):
#         self.balanc -= amount
#         return self.balanc
#
#     def deposit(self, amount):
#         self.balanc += amount
#         return self.balanc


# m1 = Bank()
# m2 = Bank()
# m1.deposit(100)
# m1.withdraw(100)


#2

class Money:
    @staticmethod
    def to_tenge(number, currency):
        if currency == "USD":
            number_tenge = number * 472
        if currency == "EUR":
            number_tenge = number * 457
        elif currency == "RUB":
            number_tenge = number * 7
        else:
            number_tenge = number

    def __str__(self):
        return f"{self.currency}"


class Wallet:
    money: [list]

    def __str__(self):
        return f"{self.money}"

    @staticmethod
    def get(index, currency):
        if currency == "USD":
            index = 1
        if currency == "EUR":
            index = 2
        elif currency == "RUB":
            index = 3
        return index

    def __add__(self, money):
        pass

    def __sizeof__(self):
        pass

    def sort(self):
        pass

    def total_balance_in_tenge(self):
        any(map(lambda number_tenge: isinstance(number_tenge, int), money))


