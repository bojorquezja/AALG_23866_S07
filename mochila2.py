class Mochila:
    def __init__(self, c, soles, kg):
        self.c = c
        self.soles = soles
        self.kg = kg
        self.ratio = soles / kg
        self.kg_cargar = 0.0
        self.me_pagan = 0.0

lista_mochila = [
    Mochila("A", 4.0, 10.0),
    Mochila("B", 3.0, 4.0),
    Mochila("C", 3.0, 7.0),
    Mochila("D", 2.0, 5.0),
    Mochila("E", 1.0, 3.0),
    Mochila("F", 2.0, 3.0),
    Mochila("G", 1.8, 2.0),
    Mochila("H", 3.0, 3.0)
]

cantidad = len(lista_mochila)
for pasada in range(cantidad):
    for actual in range(0, cantidad - pasada - 1):
        if lista_mochila[actual].ratio < lista_mochila[actual + 1].ratio:
            lista_mochila[actual], lista_mochila[actual + 1] = lista_mochila[actual + 1], lista_mochila[actual]

print("--- TABLA ORDENADA (C | S/ | Kg | S/ / Kg) ---")
for objeto in lista_mochila:
    print(f"Caja {objeto.c} | S/ {objeto.soles} | {objeto.kg} Kg | S/ / Kg: {round(objeto.ratio, 3)}")

m = float(input("\nIngrese el peso maximo m que puede llevar la mochila: "))

peso_total = 0.0
soles_totales = 0.0
seleccionadas = []

for pos in range(cantidad):
    if m == 0:
        break
        
    caja = lista_mochila[pos]

    if caja.kg <= m:
        caja.kg_cargar = caja.kg
        caja.me_pagan = caja.soles
        m = m - caja.kg
    else:
        caja.kg_cargar = m
        caja.me_pagan = caja.kg_cargar * caja.ratio
        m = 0

    peso_total = peso_total + caja.kg_cargar
    soles_totales = soles_totales + caja.me_pagan
    seleccionadas.append(caja)

print("\n--- CAJAS SELECCIONADAS ---")
for item in seleccionadas:
    print(f"Caja: {item.c} | Kg cargar: {round(item.kg_cargar, 2)} Kg | Me pagan: S/ {round(item.me_pagan, 2)}")

print(f"\nPeso total: {round(peso_total, 2)} Kg")
print(f"Soles totales: S/ {round(soles_totales, 2)}")