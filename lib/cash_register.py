#!/usr/bin/env python3

import sys
import io

class CashRegister:
    def __init__(self, discount=0):

        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):

        for _ in range(quantity):
            self.items.append(title)
        self.total += price * quantity
        self.last_transaction = (title, price, quantity)

    def apply_discount(self):

        if self.discount > 0:
            self.total -= (self.total * self.discount) / 100
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):

        if self.last_transaction:
            title, price, quantity = self.last_transaction
            self.total -= price * quantity
            for _ in range(quantity):
                self.items.remove(title)
            self.last_transaction = None

# Example usage
if __name__ == "__main__":
    # Create instances of CashRegister
    register1 = CashRegister()
    register2 = CashRegister(20)

    # Adding items to the register
    register1.add_item("eggs", 0.98)
    print(f"Register1 Total: {register1.total}")  

    register1.add_item("book", 5.00, 3)
    print(f"Register1 Total After Adding Books: {register1.total}") 

    # Applying discount
    register2.add_item("macbook air", 1000)
    register2.apply_discount()
    print(f"Register2 Total After Discount: {register2.total}") 

    # Testing void_last_transaction
    register1.add_item("apple", 1.50)
    print(f"Register1 Total Before Void: {register1.total}")  
    register1.void_last_transaction()
    print(f"Register1 Total After Void: {register1.total}")  
