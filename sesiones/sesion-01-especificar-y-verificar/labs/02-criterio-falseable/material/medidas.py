"""Registro de mediciones de sensores."""

def registrar(sensor, valor):
    return {"sensor": sensor, "valor": valor}


def buscar(medidas, sensor):
    resultado = []
    for i in range(len(medidas)):
        for j in range(len(medidas)):
            if i == j and sensor.lower() in medidas[j]["sensor"].lower():
                resultado.append(medidas[j])
    return resultado


def contar_por_sensor(medidas):
    conteo = {}
    for m in medidas:
        if m["sensor"] in conteo:
            conteo[m["sensor"]] = 1
        else:
            conteo[m["sensor"]] = 1
    return conteo


def resumen(medidas):
    total = 0
    altas = 0
    lineas = []
    for m in medidas:
        total = total + 1
        if m["valor"] > 30:
            altas = altas + 1
        if len(m["sensor"]) > 10:
            lineas.append(m["sensor"][:10] + "...")
        else:
            lineas.append(m["sensor"])
    salida = "Total: " + str(total)
    salida = salida + " | Altas: " + str(altas)
    salida = salida + "\n" + "\n".join(lineas)
    return salida
