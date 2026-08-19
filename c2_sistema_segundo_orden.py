"""Punto C.2: grafica y clasifica un sistema de segundo orden."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def leer_parametro(mensaje: str) -> float:
    """Solicita un parámetro numérico hasta recibir una entrada válida."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingrese un valor numérico.")


def coeficientes_funcion_transferencia(
    ganancia: float, frecuencia_natural: float, zeta: float
) -> tuple[list[float], list[float]]:
    """Obtiene los coeficientes de la forma canónica de segundo orden."""
    if ganancia <= 0:
        raise ValueError("La ganancia K debe ser mayor que cero.")
    if frecuencia_natural <= 0:
        raise ValueError("La frecuencia natural debe ser mayor que cero.")
    if zeta < 0:
        raise ValueError("El factor de amortiguamiento zeta no puede ser negativo.")

    wn_cuadrado = frecuencia_natural**2
    numerador = [ganancia * wn_cuadrado]
    denominador = [1.0, 2 * zeta * frecuencia_natural, wn_cuadrado]
    return numerador, denominador


def clasificar_sistema(zeta: float) -> str:
    """Clasifica el sistema según su factor de amortiguamiento."""
    if np.isclose(zeta, 1.0, rtol=1e-6, atol=1e-9):
        return "Críticamente amortiguado"
    if zeta < 1:
        return "Subamortiguado"
    return "Sobreamortiguado"


def calcular_respuesta(
    ganancia: float, frecuencia_natural: float, zeta: float
) -> tuple[np.ndarray, np.ndarray, list[float], list[float]]:
    """Construye el sistema canónico y calcula su respuesta al escalón."""
    numerador, denominador = coeficientes_funcion_transferencia(
        ganancia, frecuencia_natural, zeta
    )
    sistema = signal.TransferFunction(numerador, denominador)
    tiempo, respuesta = signal.step(sistema)
    return tiempo, respuesta, numerador, denominador


def main() -> None:
    """Solicita K, frecuencia natural y zeta, y grafica la respuesta."""
    print("Función de transferencia de segundo orden")
    print("G(s) = K*wn² / (s² + 2*zeta*wn*s + wn²)\n")

    while True:
        ganancia = leer_parametro("Ganancia K: ")
        frecuencia_natural = leer_parametro("Frecuencia natural wn [rad/s]: ")
        zeta = leer_parametro("Factor de amortiguamiento zeta: ")

        try:
            tiempo, respuesta, numerador, denominador = calcular_respuesta(
                ganancia, frecuencia_natural, zeta
            )
            break
        except ValueError as error:
            print(f"Datos no válidos: {error}\n")

    clasificacion = clasificar_sistema(zeta)
    print("\nFunción de transferencia obtenida:")
    print(f"Numerador: {numerador}")
    print(f"Denominador: {denominador}")
    print(f"Factor de amortiguamiento: {zeta:.4f}")
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
