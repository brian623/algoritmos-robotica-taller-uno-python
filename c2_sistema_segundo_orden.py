"""Punto C.2: grafica y clasifica un sistema de segundo orden."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def leer_coeficiente(mensaje: str) -> float:
    """Solicita un coeficiente numérico hasta recibir una entrada válida."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingrese un valor numérico.")


def factor_amortiguamiento(a2: float, a1: float, a0: float) -> float:
    """Calcula zeta para el denominador a2*s² + a1*s + a0."""
    if a2 <= 0 or a0 <= 0 or a1 < 0:
        raise ValueError("Se requiere a2 > 0, a0 > 0 y a1 >= 0.")
    return a1 / (2 * np.sqrt(a2 * a0))


def clasificar_sistema(zeta: float) -> str:
    """Clasifica el sistema según su factor de amortiguamiento."""
    if np.isclose(zeta, 1.0, rtol=1e-6, atol=1e-9):
        return "Críticamente amortiguado"
    if zeta < 1:
        return "Subamortiguado"
    return "Sobreamortiguado"


def calcular_respuesta(
    numerador: list[float], denominador: list[float]
) -> tuple[np.ndarray, np.ndarray]:
    """Calcula la respuesta al escalón de la función de transferencia."""
    if np.allclose(numerador, 0):
        raise ValueError("El numerador no puede tener todos sus coeficientes en cero.")
    numerador_normalizado = np.trim_zeros(np.asarray(numerador, dtype=float), "f")
    sistema = signal.TransferFunction(numerador_normalizado, denominador)
    tiempo, respuesta = signal.step(sistema)
    return tiempo, respuesta


def main() -> None:
    """Solicita coeficientes, clasifica el sistema y grafica su respuesta."""
    print("Función de transferencia de segundo orden")
    print("G(s) = (b2*s² + b1*s + b0) / (a2*s² + a1*s + a0)\n")

    while True:
        b2 = leer_coeficiente("Coeficiente b2: ")
        b1 = leer_coeficiente("Coeficiente b1: ")
        b0 = leer_coeficiente("Coeficiente b0: ")
        a2 = leer_coeficiente("Coeficiente a2: ")
        a1 = leer_coeficiente("Coeficiente a1: ")
        a0 = leer_coeficiente("Coeficiente a0: ")

        try:
            zeta = factor_amortiguamiento(a2, a1, a0)
            tiempo, respuesta = calcular_respuesta(
                [b2, b1, b0], [a2, a1, a0]
            )
            break
        except ValueError as error:
            print(f"Datos no válidos: {error}\n")

    clasificacion = clasificar_sistema(zeta)
    print(f"\nFactor de amortiguamiento: {zeta:.4f}")
    print(f"Tipo de sistema: {clasificacion}")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(tiempo, respuesta, linewidth=2, color="royalblue")
    ax.set_title(f"Respuesta al escalón - {clasificacion}")
    ax.set_xlabel("Tiempo [s]")
    ax.set_ylabel("Amplitud")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
