"""Núcleo mínimo de un procesador de eventos de pago."""

from dataclasses import dataclass, field


@dataclass
class Ledger:
    """Registra el saldo acreditado por webhooks de pago."""

    balance_cents: int = 0
    processed_event_ids: set[str] = field(default_factory=set)

    def apply_payment(self, event_id: str, amount_cents: int) -> str:
        """Aplica un evento y devuelve ``applied`` o ``ignored``."""

        self.balance_cents += amount_cents
        self.processed_event_ids.add(event_id)
        return "applied"
