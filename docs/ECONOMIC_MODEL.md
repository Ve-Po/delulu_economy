# ECONOMY.EXE — Economic Model

## 1. Purpose

The first prototype models a simplified competitive market
for one homogeneous good: bread.

The purpose is to implement and test the relationship
between demand, supply, price, and market equilibrium.

This is an educational model, not an empirically calibrated
representation of a real economy.

## 2. Model scope

- One homogeneous good: bread.
- One market.
- Price is measured in currency units per loaf.
- Quantity is measured in loaves per day.
- Demand and supply are represented by aggregate linear functions.
- The initial model assumes competitive market behaviour.
- The model is deterministic.

## 3. Demand function

Q_d = max(0, a - b * P)

Where:

- Q_d: quantity demanded per day.
- a: demand intercept.
- b: demand sensitivity to price.
- P: market price.

Assumptions:

- b > 0.
- Demand does not become negative.
- Other determinants of demand remain constant
  unless explicitly changed in an experiment.

## 4. Supply function

Q_s = max(0, c + d * P)

Where:

- Q_s: quantity supplied per day.
- c: supply intercept.
- d: supply sensitivity to price.
- P: market price.

Assumptions:

- d > 0.
- Supply does not become negative.
- Production technology and input costs remain constant
  unless explicitly changed in an experiment.

## 5. Baseline parameters

- a = 100
- b = 10
- c = -20
- d = 10

The resulting functions are:

Q_d = max(0, 100 - 10P)
Q_s = max(0, -20 + 10P)

For an interior equilibrium:

Q_d = Q_s

P* = (a - c) / (b + d)

Q* = a - bP*

Baseline equilibrium:

- P* = 6
- Q* = 40

## 6. Demand shock experiment

Increase a from 100 to 120.

Keep b, c, and d unchanged.

New equilibrium:

- P* = 7
- Q* = 50

Expected result:

An outward shift in demand increases equilibrium price
and equilibrium quantity under the model's assumptions.

## 7. Limitations

This model does not yet represent:

- Individual households or firms.
- Differences in income or preferences.
- Household budget constraints.
- Inventory and unsold goods.
- Production capacity.
- Time delays in production.
- Market power.
- Credit and money creation.
- Strategic behaviour.
- Uncertainty or expectations.

The aggregate equilibrium is a theoretical benchmark.
It is not yet a transaction-level simulation.

## 8. Research foundation

The model uses the standard introductory microeconomic
framework of demand, supply, and competitive equilibrium.

Primary learning resource:

CORE Econ — The Economy 2.0:
https://www.core-econ.org/

The model is a simplified implementation for educational
experimentation. Its parameters are illustrative and are
not estimated from real-world data.
