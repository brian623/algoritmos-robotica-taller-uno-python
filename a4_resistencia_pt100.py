"""Punto A.4: resistencia de una RTD de platino PT100."""

R0 = 100.0
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12


def resistencia_pt100(temperatura_c: float) -> float:
    """Calcula la resistencia en ohmios mediante Callendar-Van Dusen."""
    if not -200.0 <= temperatura_c <= 850.0:
        raise ValueError("La temperatura debe estar entre -200 °C y 850 °C.")

    if temperatura_c >= 0:
        return R0 * (1 + A * temperatura_c + B * temperatura_c**2)

    return R0 * (
        1
        + A * temperatura_c
        + B * temperatura_c**2
        + C * (temperatura_c - 100) * temperatura_c**3
    )


def main() -> None:
    """Calcula la resistencia para una temperatura previamente inicializada."""
    temperatura = -50.0
    resistencia = resistencia_pt100(temperatura)

    print(f"Temperatura: {temperatura:.2f} °C")
    print(f"Resistencia de la PT100: {resistencia:.4f} Ω")


if __name__ == "__main__":
    main()
