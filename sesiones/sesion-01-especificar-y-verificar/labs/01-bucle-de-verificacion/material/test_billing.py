import unittest

from billing import Ledger


class LedgerTests(unittest.TestCase):
    def test_payment_increases_balance(self) -> None:
        ledger = Ledger()

        result = ledger.apply_payment("evt-100", 2500)

        self.assertEqual(result, "applied")
        self.assertEqual(ledger.balance_cents, 2500)
        self.assertEqual(ledger.processed_event_ids, {"evt-100"})

    def test_same_event_is_applied_once(self) -> None:
        ledger = Ledger()

        first = ledger.apply_payment("evt-100", 2500)
        second = ledger.apply_payment("evt-100", 2500)

        self.assertEqual(first, "applied")
        self.assertEqual(ledger.balance_cents, 2500)
        self.assertEqual(second, "ignored")
        self.assertEqual(ledger.processed_event_ids, {"evt-100"})

    def test_different_events_are_applied(self) -> None:
        ledger = Ledger()

        ledger.apply_payment("evt-100", 2500)
        ledger.apply_payment("evt-101", 1500)

        self.assertEqual(ledger.balance_cents, 4000)
        self.assertEqual(ledger.processed_event_ids, {"evt-100", "evt-101"})


if __name__ == "__main__":
    unittest.main()
