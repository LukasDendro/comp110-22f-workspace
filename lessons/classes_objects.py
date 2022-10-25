"""xample of a class and object instantiation."""


class Pizza:
    """Models the idea of a pizza."""

    # Attribute Defintitions
    size: str
    toppings: int
    extra_cheese: False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for intialization of object."""
        self.size = size
        self.topppings = toppings

 
    def price(self, tax: float) -> float:
        """calculate the price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0
        
        total += tax

        return total


a_pizza: Pizza = Pizza("large", 3)
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")