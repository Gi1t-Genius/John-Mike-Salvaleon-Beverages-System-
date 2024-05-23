https://onlinegdb.com/Ym3uWBCWK

class Beverage:  # Abstraction
    def __init__(self, name, price):  # Encapsulation
        self.name = name
        self.price = price

    def taste(self):  # Abstraction
        return "Default Taste"  

    def describe(self):  # Abstraction
        return f"This is a {self.name} and it costs ${self.price}. It tastes {self.taste()}."

class HotBeverage(Beverage):  # Inheritance
    def __init__(self, name, price):  # Encapsulation
        super().__init__(name, price)

    def taste(self):  # Polymorphism
        return "Mmmmmm.. Hot!"

class ColdBeverage(Beverage):  # Inheritance
    def __init__(self, name, price):  # Encapsulation
        super().__init__(name, price)

    def taste(self):  # Polymorphism
        return "Mmmmmm.. Refreshing!"

hot_coffee = HotBeverage("Coffee", 3.50)  # Object
print(hot_coffee.describe())  # Object

iced_tea = ColdBeverage("Iced Tea", 2.75)  # Object
print(iced_tea.describe())  # Object

                   
