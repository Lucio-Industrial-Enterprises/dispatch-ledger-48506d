# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in dollars.

| Parameter | Description |
|-----------|-------------|
| `weight_kg` | Parcel weight in kilograms (must be positive) |
| `zone` | `"local"` or `"regional"` |
| `service` | `"standard"` (default) or `"express"` |

**Standard rates:** $5 base (local) or $8 base (regional) + $1.50 per kg.

**Express rates:** standard rate + $7 flat surcharge.

```python
from warehouse.rates import shipping_quote

shipping_quote(2, "local")                    # → 8.0  (standard)
shipping_quote(2, "local", service="express") # → 15.0 (express)
```

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
python -m warehouse.cli 2 local                    # $8.00
python -m warehouse.cli 2 local --service express  # $15.00
```
