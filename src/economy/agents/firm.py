from dataclasses import dataclass
from math import isfinite


@dataclass
class Firm:
    """
    Represents a bread-producing firm.

    Production consumes money and creates inventory.
    Sales transfer money from households to the firm.
    """

    firm_id: str
    balance: float
    inventory: float
    production_capacity: float
    unit_cost: float

    def __post_init__(self) -> None:
        if not self.firm_id.strip():
            raise ValueError("firm_id cannot be empty")

        values = {
            "balance": self.balance,
            "inventory": self.inventory,
            "production_capacity": self.production_capacity,
            "unit_cost": self.unit_cost,
        }

        for name, value in values.items():
            if not isfinite(value):
                raise ValueError(f"{name} must be finite")

        if self.balance < 0:
            raise ValueError("balance cannot be negative")
        if self.inventory < 0:
            raise ValueError("inventory cannot be negative")
        if self.production_capacity < 0:
            raise ValueError("production_capacity cannot be negative")
        if self.unit_cost < 0:
            raise ValueError("unit_cost cannot be negative")

    def produce(self, requested_quantity: float) -> float:
        """
        Produce bread, limited by capacity and available funds.

        Returns the production cost paid to the external
        input sector.
        """

        if not isfinite(requested_quantity):
            raise ValueError("requested_quantity must be finite")

        if requested_quantity < 0:
            raise ValueError("requested_quantity cannot be negative")

        if requested_quantity == 0:
            return 0.0

        if self.unit_cost == 0:
            affordable_quantity = requested_quantity
        else:
            affordable_quantity = self.balance / self.unit_cost

        quantity = min(
            requested_quantity,
            self.production_capacity,
            affordable_quantity,
        )

        cost = quantity * self.unit_cost

        self.balance -= cost
        self.inventory += quantity

        return cost

    def receive_payment(self, amount: float) -> None:
        """Credit the firm's balance after a sale."""

        if not isfinite(amount) or amount < 0:
            raise ValueError("Payment must be finite and non-negative")

        self.balance += amount
