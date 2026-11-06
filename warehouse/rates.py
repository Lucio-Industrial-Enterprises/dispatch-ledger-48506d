"""Shipping rate calculations."""

_SERVICES = {"standard", "express"}
_EXPRESS_SURCHARGE = 7.0


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone – ``"local"`` or ``"regional"``.
        service: Service level – ``"standard"`` (default) or ``"express"``.
            Express adds a flat $7 surcharge on top of the standard rate.

    Returns:
        Total shipping cost in dollars, rounded to two decimal places.

    Raises:
        ValueError: If *weight_kg* is not positive, *zone* is unrecognised,
            or *service* is unrecognised.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in _SERVICES:
        raise ValueError(f"unknown service: {service!r}")
    base = 5.0 if zone == "local" else 8.0
    surcharge = _EXPRESS_SURCHARGE if service == "express" else 0.0
    return round(base + 1.5 * weight_kg + surcharge, 2)
