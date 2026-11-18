from datetime import date, time
import unittest

from study import effective_close, implied, payoff, remaining_cash


class SpreadTests(unittest.TestCase):
    def test_after_early_close_maps_to_monday(self):
        friday, monday = date(2023, 11, 24), date(2023, 11, 27)
        sessions = {friday: time(13), monday: time(16)}
        self.assertEqual(effective_close(friday, time(14), sessions), monday)
        self.assertEqual(effective_close(friday, time(12, 59), sessions), friday)

    def test_payment_cap(self):
        self.assertAlmostEqual(remaining_cash(33.50, 2.50, 12), 29.85)
        self.assertAlmostEqual(remaining_cash(33.50, 2.50, 4), 30.60)

    def test_break_only_at_state_value(self):
        self.assertEqual(implied(8, 30, 8), (0, True))
        self.assertEqual(implied(7, 30, 8), (-1/22, False))
        self.assertEqual(implied(7, 8, 8), (None, False))

    def test_future_cash_is_discounted_to_earlier_receipt(self):
        self.assertAlmostEqual(payoff(30, 90, 15) - payoff(30, 90),
                               sum(.10/1.05**(day/365) for day in (15,45,75)))
