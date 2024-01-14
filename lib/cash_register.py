#!/usr/bin/env python3

# class CashRegister:
#     def __init__(self, discount=0):
#         self.total = 0
#         self.items = []
#         self.discount = discount

#     def add_item(self, title, price, quantity=1):
#         self.total += price * quantity
#         self.items.extend([title] * quantity)

#     def apply_discount(self):
#         if self.discount > 0:
#             # Convert total to a float before applying the discount
#             self.total = float(self.total) * (1 - self.discount / 100)
#             print(f"After the discount, the total comes to ${int(self.total)}.")
#         else:
#             print("There is no discount to apply.")

#     def void_last_transaction(self, price):
#         if self.items:
#             last_item_price = self.total - sum([price[item] for item in self.items[:-1]])
#             self.total -= last_item_price
#             self.items.pop()
#         else:
#             print("No transactions to void.")

# class CashRegister:
#     def __init__(self, discount=0):
#         self.total = 0
#         self.items = []
#         self.discount = discount

#     def add_item(self, title, price, quantity=1):
#         item = (title, price, quantity)
#         self.items.append(item)
#         self.total += price * quantity

#     def apply_discount(self):
#         if self.discount > 0:
#             self.total = float(self.total) * (1 - self.discount / 100)
#             print(f"After the discount, the total comes to ${int(self.total)}.")
#         else:
#             print("There is no discount to apply.")

#     def void_last_transaction(self):
#         if self.items:
#             last_item = self.items.pop()
#             last_item_price = last_item[1] * last_item[2]
#             self.total -= last_item_price
#         else:
#             print("No transactions to void.")

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        item = {'title': title, 'price': price, 'quantity': quantity}
        self.items.append(item)
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            self.total = float(self.total) * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            last_item_price = last_item['price'] * last_item['quantity']
            self.total -= last_item_price
        else:
            print("No transactions to void.")

