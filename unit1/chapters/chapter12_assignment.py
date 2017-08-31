class Car:
    def __init__(self, gas_level):
        self.gas_level = gas_level

    def add_gas(self, amount):
        self.gas_level += amount

    def fill_up(self):
        amount = 13 - self.gas_level
        if self.gas_level < 13:
            self.add_gas(amount)
            return amount
        else:
            return 0
