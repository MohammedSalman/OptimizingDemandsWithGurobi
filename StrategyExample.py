import abc
from typing import List


class StrategyExample:
    def __init__(self, billing_strategy: "BillingStrategy"):
        self.drinks: List[float] = []
        self._billing_strategy = billing_strategy

    @property
    def billing_strategy(self) -> "BillingStrategy":
        return self._billing_strategy

    @billing_strategy.setter
    def billing_strategy(self, billing_strategy: "BillingStrategy") -> None:
        self._billing_strategy = billing_strategy

    def add(self, price: float, quantity: int) -> None:
        self.drinks.append(self.billing_strategy.get_act_price(price * quantity))

    def __str__(self) -> str:
        return str(f"£{sum(self.drinks)}")


class BillingStrategy(abc.ABC):
    @abc.abstractmethod
    def get_act_price(self, raw_price: float) -> float:
        raise NotImplementedError


class NormalStrategy(BillingStrategy):
    def get_act_price(self, raw_price: float) -> float:
        return raw_price


class HappyHourStrategy(BillingStrategy):
    def get_act_price(self, raw_price: float) -> float:
        return raw_price * 0.5


def main() -> None:
    normal_strategy = NormalStrategy()
    happy_hour_strategy = HappyHourStrategy()

    customer_1 = StrategyExample(normal_strategy)
    customer_2 = StrategyExample(normal_strategy)

    # Normal billing
    customer_1.add(2.50, 3)
    customer_1.add(2.50, 2)

    # Start happy hour
    customer_1.billing_strategy = happy_hour_strategy
    customer_2.billing_strategy = happy_hour_strategy
    customer_1.add(3.40, 6)
    customer_2.add(3.10, 2)

    # End happy hour
    customer_1.billing_strategy = normal_strategy
    customer_2.billing_strategy = normal_strategy
    customer_1.add(3.10, 6)
    customer_2.add(3.10, 2)

    # Print the bills;
    print(customer_1)
    print(customer_2)


if __name__ == "__main__":
    main()
