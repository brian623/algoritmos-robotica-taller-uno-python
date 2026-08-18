"""Punto B.2: genera números enteros aleatorios en un rango dado."""

from random import randint


def leer_entero(mensaje: str) -> int:
    """Solicita un número entero hasta recibir una entrada válida."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")


def generar_numeros(cantidad: int, minimo: int, maximo: int) -> list[int]:
    """Genera la cantidad indicada de enteros dentro del intervalo cerrado."""
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")
    if minimo > maximo:
        raise ValueError("El límite mínimo no puede superar al máximo.")

    return [randint(minimo, maximo) for _ in range(cantidad)]


def main() -> None:
    """Solicita los parámetros y muestra los números generados."""
    print("Generador de números enteros aleatorios")

    while True:
        cantidad = leer_entero("Cantidad de números: ")
        minimo = leer_entero("Límite mínimo: ")
        maximo = leer_entero("Límite máximo: ")

        try:
            numeros = generar_numeros(cantidad, minimo, maximo)
            break
        except ValueError as error:
            print(f"Datos no válidos: {error}\n")

    print(f"\nNúmeros generados: {numeros}")


if __name__ == "__main__":
    main()
