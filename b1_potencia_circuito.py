"""Punto B.1: calcula la potencia eléctrica con datos del usuario."""


def leer_numero(mensaje: str) -> float:
    """Solicita un número y repite la pregunta si la entrada no es válida."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingrese un valor numérico.")


def calcular_potencia(voltaje: float, corriente: float) -> float:
    """Calcula la potencia eléctrica mediante P = V * I."""
    return voltaje * corriente


def main() -> None:
    """Solicita voltaje y corriente, y muestra la potencia consumida."""
    print("Cálculo de potencia eléctrica")
    voltaje = leer_numero("Ingrese el voltaje [V]: ")
    corriente = leer_numero("Ingrese la corriente [A]: ")

    potencia = calcular_potencia(voltaje, corriente)
    print(f"\nPotencia consumida: {potencia:.2f} W")


if __name__ == "__main__":
    main()
