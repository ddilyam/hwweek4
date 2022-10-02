# 1
# balance = 0
#
# def deposit(amount):
#     global balance
#     balance += amount
#     return f'BALANCE: {balance}'
#
# def withdraw(amount):
#     global balance
#     balance -= amount
#     return f'BALANCE: {balance}'
#
# class Bank:
#     def __init__(self, amount):
#         self.amount = amount
# bank = Bank(int(input("Enter number of money that you deposite/withdraw: ")))
# while(True):
#     print("press '1' to add money\n" "press '2' to withdraw\n" )
#     num = int(input())
#     if num==1:
#         print(deposit(bank.amount))
#     elif num==2:
#         print(withdraw(bank.amount))
#     else:
#         print("incorrect input")

#2

# class Money:
#
#     def __init__(self, number, amount, currency):
#         self.number = number
#         self.currency = currency
#         self.amount = amount
#
#
#     def to_tenge(self):
#         if (self.currency == "usd"):
#             return  self.number * self.amount * 472
#         elif (self.currency == "eur"):
#             return self.number * self.amount * 457
#         elif (self.currency == "rub"):
#             return self.number * self.amount * 7
#         elif (self.currency == "tng"):
#             return self.number * self.number
#         else:
#             print("Error!")
#
#     def get(self):
#         return f"{self.amount} pcs {self.number} {self.currency}"
#
#
# class Wallet():
#
#     def __init__(self, m):
#         self.money = []
#         self.money.append(Money.get(m))
#
#     def get(self, x):
#         print(self.money[x])
#
#     def add(self, m):
#         self.money.append(Money.get(m))
#
#     def sort(self, y):
#         self.money[y]
#
#     def size(self):
#         for name in range(len(self.money)):
#             print(f' The index {name} for {self.money[name]}')
#
#     def __str__(self):
#         return self.money
#
# x=Money(30,10,"usd")
# y=Money(13,10,"eur")
# z=Money(15,10,"rub")
# w=Money(20,10,"tng")
# m=Wallet(x)
# m.add(y)
# m.add(z)
# m.add(w)
# print(m.__str__())
# m.size()
# w=[x.to_tenge(),y.to_tenge(),z.to_tenge(),w.to_tenge()]
# print(f'total balance: {sum(w)}')
