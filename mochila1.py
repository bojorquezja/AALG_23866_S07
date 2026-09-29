# MOCHILA FRACCIONARIA - MÉTODO VORAZ

# Datos de las cajas
cajas = [
    {"nombre": "A", "peso": 10, "valor": 4},
    {"nombre": "B", "peso": 4, "valor": 3},
    {"nombre": "C", "peso": 7, "valor": 3},
    {"nombre": "D", "peso": 5, "valor": 2},
    {"nombre": "E", "peso": 3, "valor": 1},
    {"nombre": "F", "peso": 3, "valor": 2},
    {"nombre": "G", "peso": 2, "valor": 1.8},
    {"nombre": "H", "peso": 3, "valor": 3}
]

# Ingreso de la capacidad de la mochila
capacidad = float(input("Ingrese la capacidad máxima de la mochila (kg): "))

# Calcular valor por kilogramo
for caja in cajas:
    caja["valor_por_kg"] = caja["valor"] / caja["peso"]

# Ordenar de mayor a menor según valor por kg
cajas.sort(key=lambda x: x["valor_por_kg"], reverse=True)

peso_total = 0
valor_total = 0
seleccionadas = []

# Algoritmo voraz
for caja in cajas:

    if peso_total + caja["peso"] <= capacidad:

        seleccionadas.append({
            "nombre": caja["nombre"],
            "peso": caja["peso"],
            "valor": caja["valor"],
            "fraccion": 1
        })

        peso_total += caja["peso"]
        valor_total += caja["valor"]

    else:
        espacio_disponible = capacidad - peso_total

        if espacio_disponible > 0:

            fraccion = espacio_disponible / caja["peso"]

            seleccionadas.append({
                "nombre": caja["nombre"],
                "peso": espacio_disponible,
                "valor": caja["valor"] * fraccion,
                "fraccion": fraccion
            })

            peso_total += espacio_disponible
            valor_total += caja["valor"] * fraccion

        break

# Mostrar datos originales
print("\n" + "=" * 70)
print("             METODO VORAZ - MOCHILA FRACCIONARIA")
print("=" * 70)

print("\nDATOS DE LAS CAJAS")
print("-" * 70)
print(f"{'Caja':<10}{'Peso(kg)':<15}{'Valor(S/)':<15}{'Valor/Kg':<15}")

for caja in cajas:
    print(
        f"{caja['nombre']:<10}"
        f"{caja['peso']:<15}"
        f"{caja['valor']:<15}"
        f"{caja['valor_por_kg']:.2f}"
    )

# Mostrar selección
print("\nCAJAS SELECCIONADAS")
print("-" * 70)
print(f"{'Caja':<10}{'Peso Usado':<15}{'Valor':<15}{'Uso'}")

for item in seleccionadas:
    print(
        f"{item['nombre']:<10}"
        f"{item['peso']:<15.2f}"
        f"{item['valor']:<15.2f}"
        f"{item['fraccion']*100:.2f}%"
    )

print("-" * 70)
print(f"Capacidad de la mochila : {capacidad:.2f} kg")
print(f"Peso total utilizado    : {peso_total:.2f} kg")
print(f"Valor total obtenido    : S/ {valor_total:.2f}")

print("=" * 70)