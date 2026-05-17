# In this workshop, you are going to build a discount calculator that can apply different discount strategies to products.
# The system will determine the best price for a customer based on multiple discount rules.

from abc import ABC, abstractmethod

class Product:
    # Represents a product with a name and price
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    # Returns a string representation of the product
    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'

class DiscountStrategy(ABC):
    # Abstract base class for discount strategies
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass

class PercentageDiscount(DiscountStrategy):
    # Represents a percentage-based discount strategy
    def __init__(self, percent: int) -> None:
        self.percent = percent

    # Returns True if the discount is applicable for the given product and user tier
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= 70

    # Applies the percentage-based discount to the product price
    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)

class FixedAmountDiscount(DiscountStrategy):
    # Represents a fixed-amount-based discount strategy
    def __init__(self, amount: int) -> None:
        self.amount = amount

    # Returns True if the discount is applicable for the given product and user tier
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount

    # Applies the fixed-amount-based discount to the product price
    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount

class PremiumUserDiscount(DiscountStrategy):
    # Represents a premium user-based discount strategy
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    # Applies the premium user-based discount to the product price
    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8

class DiscountEngine:
    # Manages a list of discount strategies and calculates the best price for a product based on user tier
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        self.strategies = strategies

    # Calculates the best price for a product based on the given discount strategies and user tier
    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        return min(prices)

if __name__ == '__main__':
    # Example usage: calculates the best price for a product based on multiple discount strategies and user tier
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'

    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)
    print(f"Best price for {product.name} for {user_tier} user: ${best_price:.2f}")