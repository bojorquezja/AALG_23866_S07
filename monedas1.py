# LISTA DE DENOMINACIONES
denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]

# ENTRADA
monto = float(input(" Ingrese el monto a pagar: S/ "))

# VARIABLE AUXILIAR
restante = monto

# ENCABEZADO
print("\n" + "=" * 45)
print("     DESGLOSE DE BILLETES Y MONEDAS")
print("=" * 45)
print(f"{'Denominación':<15}{'Cantidad':<12}{'Restante'}")
print("-" * 45)

# RECORRER DENOMINACIONES
for d in denominaciones:

    cantidad = int(restante // d)

    if cantidad > 0:

        restante = restante + 0.000000001 - (cantidad * d)
        #restante = round(restante, 2)

        print(f"S/{d:<13}{cantidad:<12}{restante}")

# RESULTADO FINAL
print("-" * 45)
print(f"Vuelto final: S/{restante}")
print("=" * 45)