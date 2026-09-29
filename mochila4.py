def mochila_fraccionaria(capacidad, cajas):
    cajas.sort(key=lambda x: x['soles'] / x['peso'], reverse=True)

    peso_total = soles_totales = 0
    seleccion = []

    for c in cajas:
        if peso_total >= capacidad:
            break
        
        peso_tomado = min(c['peso'], capacidad - peso_total)
        soles = peso_tomado * (c['soles'] / c['peso'])

        peso_total += peso_tomado
        soles_totales += soles
        seleccion.append((c['nombre'], peso_tomado, soles))

    return seleccion, peso_total, soles_totales


# Datos
m = float(input("Peso máximo: ") or 20)
cajas = [
    {'nombre': 'A', 'peso': 10, 'soles': 4},
    {'nombre': 'B', 'peso': 4,  'soles': 3},
    {'nombre': 'C', 'peso': 7,  'soles': 3},
    {'nombre': 'D', 'peso': 5,  'soles': 2},
    {'nombre': 'E', 'peso': 3,  'soles': 1},
    {'nombre': 'F', 'peso': 3,  'soles': 2},
    {'nombre': 'G', 'peso': 2,  'soles': 1.8},
    {'nombre': 'H', 'peso': 3,  'soles': 3},
]

items, p_tot, s_tot = mochila_fraccionaria(m, cajas)

print("\nCajas elegidas (Nombre, Kg tomados, Soles ganados):")
for item in items:
    print(f"Caja {item[0]}: {item[1]:.2f} Kg -> S/ {item[2]:.2f}")

print(f"\nPeso Total: {p_tot:.2f} Kg | Soles Totales: S/ {s_tot:.2f}")