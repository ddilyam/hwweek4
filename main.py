# 1
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


#2

class Money:

    def __init__(self, number, amount, currency):
        self.number = number
        self.currency = currency
        self.amount = amount


    def to_tenge(self):
        if (self.currency == "USD"):
            return  self.number * self.amount * 472
        elif (self.currency == "EUR"):
            return self.number * self.amount * 457
        elif (self.currency == "RUB"):
            return self.number * self.amount * 7
        elif (self.currency == "TNG"):
            return self.number * self.number
        else:
            print("Error!")

    def __str__(self):
        return f"{self.amount} of {self.number} {self.currency}"


class Wallet:

    def __init__(self, m):
        self.money = []
        self.money.append(Money.get(m))

    def get(self, x):
        print(self.money[x])

    def add(self, m):
        self.money.append(Money.get(m))

    def sort(self, y):
        self.money[y]

    def size(self):
        for name in range(len(self.money)):
            print(f' The index {name} for {self.money[name]}')

    def __str__(self):
        return self.money



    # def total_balance_in_tenge(self, money) -> float:
    #     total_balance = (sum((int(money[i]) for i in range(0, int(len(money))))))
    #     print(total_balance)


