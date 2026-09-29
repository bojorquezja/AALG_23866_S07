def ordenar(cajas, clave, descendente):
    lista = cajas[:]
    n = len(lista)
    for i in range(n - 1):
        elegido = i
        for j in range(i + 1, n):
            if descendente:
                if clave(lista[j]) > clave(lista[elegido]):
                    elegido = j
            else:
                if clave(lista[j]) < clave(lista[elegido]):
                    elegido = j
        lista[i], lista[elegido] = lista[elegido], lista[i]
    return lista


def mochila_voraz(cajas, m, clave, descendente):
    ordenadas = ordenar(cajas, clave, descendente)
    elegidas = []
    peso_total = 0.0
    soles_total = 0.0

    for caja in ordenadas:
        espacio = m - peso_total
        if espacio <= 0:
            break

        if caja["peso"] <= espacio:
            fraccion = 1.0                        
        else:
            fraccion = espacio / caja["peso"]     

        peso_usado = caja["peso"] * fraccion
        soles_ganados = caja["soles"] * fraccion
        peso_total += peso_usado
        soles_total += soles_ganados
        elegidas.append((caja["nombre"], fraccion, peso_usado, soles_ganados))

    return elegidas, peso_total, soles_total


# ----------------- Datos del profesor -----------------
cajas = [
    {"nombre": "A", "peso": 10, "soles": 4},
    {"nombre": "B", "peso": 4,  "soles": 3},
    {"nombre": "C", "peso": 7,  "soles": 3},
    {"nombre": "D", "peso": 5,  "soles": 2},
    {"nombre": "E", "peso": 3,  "soles": 1},
    {"nombre": "F", "peso": 3,  "soles": 2},
    {"nombre": "G", "peso": 2,  "soles": 1.8},
    {"nombre": "H", "peso": 3,  "soles": 3},
]

m = float(input("Ingrese el peso máximo que puede llevar la mochila: "))

criterios = [
    ("De menos a más peso",        lambda c: c["peso"],                False),
    ("De más a menos peso",        lambda c: c["peso"],                True),
    ("De más a menos precio",      lambda c: c["soles"],               True),
    ("De más a menos precio/peso", lambda c: c["soles"] / c["peso"],   True),
]

print("\n--- Comparación de criterios ---")
for nombre, clave, desc in criterios:
    _, peso, soles = mochila_voraz(cajas, m, clave, desc)
    print(f"{nombre:28s} -> peso = {peso:.2f} | soles = {soles:.2f}")

nombre, clave, desc = criterios[3]
elegidas, peso_total, soles_total = mochila_voraz(cajas, m, clave, desc)

print(f"\n--- Cajas seleccionadas ({nombre}) ---")
for nom, fraccion, peso, soles in elegidas:
    print(f"Caja {nom}: {fraccion * 100:.1f}% | peso = {peso:.2f} Kg | soles = S/ {soles:.2f}")

print(f"\nPeso total: {peso_total:.2f} Kg")
print(f"Soles totales: S/ {soles_total:.2f}")