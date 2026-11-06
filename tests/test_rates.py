import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (preserved behaviour)
    # ------------------------------------------------------------------

    def test_standard_local(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)

    def test_standard_regional(self):
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_keyword(self):
        """Passing service='standard' explicitly must match the default."""
        self.assertEqual(
            shipping_quote(2, "local", service="standard"),
            shipping_quote(2, "local"),
        )

    # ------------------------------------------------------------------
    # Express service
    # ------------------------------------------------------------------

    def test_express_local(self):
        # standard local for 2 kg = 8.0, +7 express surcharge = 15.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # standard regional for 2 kg = 11.0, +7 = 18.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_fractional_weight(self):
        # local: 5.0 + 1.5*1.5 + 7.0 = 14.25
        self.assertEqual(shipping_quote(1.5, "local", service="express"), 14.25)

    # ------------------------------------------------------------------
    # Error cases
    # ------------------------------------------------------------------

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
