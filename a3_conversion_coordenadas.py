"""Punto A.3: conversión de coordenadas rectangulares."""

from math import acos, atan2, degrees, sqrt


def rectangulares_a_cilindricas(
    x: float, y: float, z: float
) -> tuple[float, float, float]:
    """Convierte (x, y, z) en (radio, azimut, altura)."""
    radio = sqrt(x**2 + y**2)
    azimut = atan2(y, x)
    return radio, azimut, z


def rectangulares_a_esfericas(
    x: float, y: float, z: float
) -> tuple[float, float, float]:
    """Convierte (x, y, z) en (radio, azimut, ángulo polar)."""
    radio = sqrt(x**2 + y**2 + z**2)
    if radio == 0:
        return 0.0, 0.0, 0.0

    azimut = atan2(y, x)
    angulo_polar = acos(z / radio)
    return radio, azimut, angulo_polar


def main() -> None:
    """Convierte y muestra un punto rectangular previamente inicializado."""
    x, y, z = 3.0, 4.0, 5.0

    radio_c, azimut_c, altura = rectangulares_a_cilindricas(x, y, z)
    radio_e, azimut_e, polar_e = rectangulares_a_esfericas(x, y, z)

    print(f"Coordenadas rectangulares: (x, y, z) = ({x}, {y}, {z})")
    print("\nCoordenadas cilíndricas:")
    print(f"Radio: {radio_c:.4f}")
    print(f"Azimut: {degrees(azimut_c):.4f}°")
    print(f"Altura: {altura:.4f}")
    print("\nCoordenadas esféricas:")
    print(f"Radio: {radio_e:.4f}")
    print(f"Azimut: {degrees(azimut_e):.4f}°")
    print(f"Ángulo polar: {degrees(polar_e):.4f}°")


if __name__ == "__main__":
    main()
