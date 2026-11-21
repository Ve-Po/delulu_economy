
import pytest

from economy.markets.linear_market import LinearMarket, Equilibrium


@pytest.fixture
def market():
    """Create the baseline bread market."""
    return LinearMarket(a=100, b=10, c=-20, d=10)


def test_calculate_demand(market):
    assert market.calculate_demand(6) == 40


def test_calculate_supply(market):
    assert market.calculate_supply(6) == 40


def test_calculate_equilibrium(market):
    equilibrium = market.calculate_equilibrium()

    assert isinstance(equilibrium, Equilibrium)
    assert equilibrium.price == pytest.approx(6)
    assert equilibrium.quantity == pytest.approx(40)


def test_equilibrium_clears_the_market(market):
    equilibrium = market.calculate_equilibrium()

    demand = market.calculate_demand(equilibrium.price)
    supply = market.calculate_supply(equilibrium.price)

    assert demand == pytest.approx(supply)


def test_demand_decreases_when_price_increases(market):
    demand_at_5 = market.calculate_demand(5)
    demand_at_6 = market.calculate_demand(6)

    assert demand_at_5 > demand_at_6


def test_supply_increases_when_price_increases(market):
    supply_at_5 = market.calculate_supply(5)
    supply_at_6 = market.calculate_supply(6)

    assert supply_at_5 < supply_at_6


def test_demand_shock_increases_equilibrium_price_and_quantity():
    market = LinearMarket(a=120, b=10, c=-20, d=10)

    equilibrium = market.calculate_equilibrium()

    assert equilibrium.price == pytest.approx(7)
    assert equilibrium.quantity == pytest.approx(50)


def test_negative_price_is_rejected(market):
    with pytest.raises(ValueError):
        market.calculate_demand(-1)


def test_invalid_demand_slope_is_rejected():
    with pytest.raises(ValueError):
        LinearMarket(a=100, b=0, c=-20, d=10)


def test_non_finite_parameter_is_rejected():
    with pytest.raises(ValueError):
        LinearMarket(a=float("nan"), b=10, c=-20, d=10)


def test_infeasible_interior_equilibrium_is_rejected():
    market = LinearMarket(a=10, b=10, c=20, d=10)

    with pytest.raises(ValueError):
        market.calculate_equilibrium()
