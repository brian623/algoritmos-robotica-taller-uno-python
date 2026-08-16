"""Punto A.6: fuerzas de un cilindro neumático de doble efecto."""

from math import pi

BAR_A_PASCAL = 100_000
MILIMETRO_A_METRO = 0.001


def calcular_fuerzas(
    presion_bar: float, diametro_piston_mm: float, diametro_vastago_mm: float
) -> tuple[float, float]:
    """Calcula las fuerzas teóricas de avance y retroceso en newtons."""
    if presion_bar <= 0:
        raise ValueError("La presión debe ser mayor que cero.")
    if diametro_piston_mm <= 0 or diametro_vastago_mm <= 0:
        raise ValueError("Los diámetros deben ser mayores que cero.")
    if diametro_vastago_mm >= diametro_piston_mm:
        raise ValueError("El vástago debe tener menor diámetro que el pistón.")

    presion_pa = presion_bar * BAR_A_PASCAL
    diametro_piston_m = diametro_piston_mm * MILIMETRO_A_METRO
    diametro_vastago_m = diametro_vastago_mm * MILIMETRO_A_METRO

    area_piston = pi * diametro_piston_m**2 / 4
    area_vastago = pi * diametro_vastago_m**2 / 4
    area_anular = area_piston - area_vastago

    fuerza_avance = presion_pa * area_piston
    fuerza_retroceso = presion_pa * area_anular
    return fuerza_avance, fuerza_retroceso


def main() -> None:
    """Calcula las fuerzas usando valores previamente establecidos."""
    presion = 6.0
    diametro_piston = 50.0
    diametro_vastago = 20.0

    fuerza_avance, fuerza_retroceso = calcular_fuerzas(
        presion, diametro_piston, diametro_vastago
    )

    print(f"Presión de trabajo: {presion:.2f} bar")
    print(f"Diámetro del pistón: {diametro_piston:.2f} mm")
    print(f"Diámetro del vástago: {diametro_vastago:.2f} mm")
    print(f"\nFuerza teórica de avance: {fuerza_avance:.2f} N")
    print(f"Fuerza teórica de retroceso: {fuerza_retroceso:.2f} N")


if __name__ == "__main__":
    main()
