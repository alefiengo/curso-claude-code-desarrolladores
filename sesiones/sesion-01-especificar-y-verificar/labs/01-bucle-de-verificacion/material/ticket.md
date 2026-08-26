# INC-247: un webhook reintentado acredita el pago dos veces

El proveedor puede entregar más de una vez el mismo evento. En producción, dos
entregas con `event_id = "evt-100"` incrementaron dos veces el saldo.

## Comportamiento esperado

- La primera entrega de un `event_id` devuelve `"applied"` y acredita el importe.
- Las entregas siguientes del mismo `event_id` devuelven `"ignored"` y no cambian el saldo.
- Dos identificadores distintos se procesan de forma independiente.
- Se conserva la firma pública de `Ledger.apply_payment`.

## Fuera de alcance

- Persistencia entre procesos.
- Concurrencia.
- Validación criptográfica de la firma del proveedor.
- Transporte HTTP.

## Verificación

```bash
python3 -m unittest -v
```
