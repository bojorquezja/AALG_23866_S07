def voraz(monto):
    denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05]
    cantidades = []

    monto = int(monto * 100)

    for denominacion in denominaciones:
        valor = int(denominacion * 100)
        cantidad = monto // valor
        cantidades.append(cantidad)
        monto = monto % valor
        if cantidad > 0:
            soles = monto // 100
            centavos = monto % 100

            restante = str(soles) + "." + str(centavos).zfill(2)

            print(f"S/{denominacion:<5} {cantidad:<3} {restante:>8}")

    return cantidades


monto = 179.45

respuesta = voraz(monto)