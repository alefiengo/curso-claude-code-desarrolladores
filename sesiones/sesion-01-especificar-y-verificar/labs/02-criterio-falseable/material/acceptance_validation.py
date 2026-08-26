"""Comprobación independiente del contrato de VAL-118."""

from billing import Ledger


INVALID_EVENTS = (
    ("", 100),
    ("   ", 100),
    (None, 100),
    (123, 100),
    ("evt-200", 0),
    ("evt-200", -1),
    ("evt-200", True),
    ("evt-200", 1.5),
)


def main() -> None:
    for event_id, amount_cents in INVALID_EVENTS:
        ledger = Ledger(balance_cents=700, processed_event_ids={"evt-existing"})
        before = (ledger.balance_cents, set(ledger.processed_event_ids))

        try:
            ledger.apply_payment(event_id, amount_cents)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Se aceptó un evento inválido: {event_id=!r}, {amount_cents=!r}"
            )

        after = (ledger.balance_cents, ledger.processed_event_ids)
        if after != before:
            raise AssertionError("Un evento rechazado modificó el estado")

    ledger = Ledger()
    first = ledger.apply_payment("evt-200", 100)
    second = ledger.apply_payment("evt-200", 100)
    if (first, second, ledger.balance_cents) != ("applied", "ignored", 100):
        raise AssertionError("La validación nueva rompió la idempotencia anterior")
    print("OK: contrato VAL-118 verificado")


if __name__ == "__main__":
    main()
