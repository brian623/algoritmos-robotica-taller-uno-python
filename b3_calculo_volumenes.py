"""Punto B.3: calcula el volumen del sólido elegido por el usuario."""

from math import pi


def leer_positivo(mensaje: str) -> float:
    """Solicita un número real estrictamente positivo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Entrada no válida. Ingrese un valor numérico.")


def volumen_prisma(largo: float, ancho: float, altura: float) -> float:
    """Calcula el volumen de un prisma rectangular."""
    return largo * ancho * altura


def volumen_piramide(area_base: float, altura: float) -> float:
    """Calcula el volumen de una pirámide a partir del área de su base."""
    return area_base * altura / 3


def volumen_cono_truncado(
    radio_mayor: float, radio_menor: float, altura: float
) -> float:
    """Calcula el volumen de un tronco de cono circular recto."""
    return (
        pi
        * altura
        * (radio_mayor**2 + radio_mayor * radio_menor + radio_menor**2)
        / 3
    )


def volumen_cilindro(radio: float, altura: float) -> float:
    """Calcula el volumen de un cilindro circular recto."""
    return pi * radio**2 * altura


def seleccionar_solido() -> str:
    """Muestra el menú hasta que el usuario seleccione una opción válida."""
    opciones = {"1", "2", "3", "4"}
    while True:
        print("\n1. Prisma rectangular")
        print("2. Pirámide")
        print("3. Cono truncado")
        print("4. Cilindro")
        opcion = input("Seleccione un sólido: ").strip()
        if opcion in opciones:
            return opcion
        print("Opción no válida. Seleccione un número del 1 al 4.")


def main() -> None:
    """Solicita el sólido y sus dimensiones, y muestra el volumen."""
    print("Cálculo de volúmenes")
    opcion = seleccionar_solido()

    if opcion == "1":
        largo = leer_positivo("Largo: ")
        ancho = leer_positivo("Ancho: ")
        altura = leer_positivo("Altura: ")
        nombre = "prisma rectangular"
        volumen = volumen_prisma(largo, ancho, altura)
    elif opcion == "2":
        area_base = leer_positivo("Área de la base: ")
        altura = leer_positivo("Altura: ")
        nombre = "pirámide"
        volumen = volumen_piramide(area_base, altura)
    elif opcion == "3":
        radio_mayor = leer_positivo("Radio mayor: ")
        radio_menor = leer_positivo("Radio menor: ")
        altura = leer_positivo("Altura: ")
        nombre = "cono truncado"
        volumen = volumen_cono_truncado(radio_mayor, radio_menor, altura)
    else:
        radio = leer_positivo("Radio: ")
        altura = leer_positivo("Altura: ")
        nombre = "cilindro"
        volumen = volumen_cilindro(radio, altura)

    print(f"\nVolumen del {nombre}: {volumen:.4f} unidades³")


if __name__ == "__main__":
    main()
