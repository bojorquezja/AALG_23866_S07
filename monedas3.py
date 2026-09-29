def pagar_con_denominaciones(denominaciones, monto):
    
    ordenadas = sorted(
        [(valor, i) for i, valor in enumerate(denominaciones)],
        reverse=True
    )

    cantidades = [0] * len(denominaciones)
    restante = monto

    for valor, indice in ordenadas:
        cantidades[indice] = restante  // valor
        restante = (restante + 0.00000001) % valor

    return cantidades, restante


def main():
    denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]

    denominaciones_cent = [round(d * 100) for d in denominaciones]

    try:
        monto = float(input("Ingrese el monto a pagar: S/ "))
    except ValueError:
        print("Monto inválido.")
        return

    if monto < 0:
        print("El monto no puede ser negativo.")
        return

    monto_cent = round(monto * 100)
    cantidades, sobrante = pagar_con_denominaciones(denominaciones_cent, monto_cent)

    print("\nDenominaciones:", denominaciones)
    print("Cantidades:    ", cantidades)

    print("\nDetalle:")
    for i in range(len(denominaciones)):
        if cantidades[i] > 0:
            print(f"  {cantidades[i]} x S/ {denominaciones[i]:.2f}")

    if sobrante > 0:
        print(f"\nNo se pudo cubrir S/ {sobrante / 100:.2f} con estas denominaciones.")


if __name__ == "__main__":
    main()