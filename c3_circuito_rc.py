"""Punto C.3: grafica la carga y descarga de un circuito RC."""

import matplotlib.pyplot as plt
import numpy as np


def leer_positivo(mensaje: str) -> float:
    """Solicita un valor numérico estrictamente positivo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Entrada no válida. Ingrese un valor numérico.")


def calcular_curvas_rc(
    voltaje: float, capacitancia_uf: float, resistencia_ohm: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Calcula tiempo, carga, descarga y constante de tiempo del circuito."""
    if voltaje <= 0 or capacitancia_uf <= 0 or resistencia_ohm <= 0:
        raise ValueError("Voltaje, capacitancia y resistencia deben ser positivos.")

    capacitancia_f = capacitancia_uf * 1e-6
    tau = resistencia_ohm * capacitancia_f
    tiempo = np.linspace(0, 5 * tau, 500)
    carga = voltaje * (1 - np.exp(-tiempo / tau))
    descarga = voltaje * np.exp(-tiempo / tau)
    return tiempo, carga, descarga, tau


def main() -> None:
    """Solicita los datos del circuito y muestra sus curvas transitorias."""
    print("Carga y descarga de un circuito RC")
    voltaje = leer_positivo("Voltaje de la fuente [V]: ")
    capacitancia = leer_positivo("Capacitancia [µF]: ")
    resistencia = leer_positivo("Resistencia [Ω]: ")

    tiempo, carga, descarga, tau = calcular_curvas_rc(
        voltaje, capacitancia, resistencia
    )
    print(f"\nConstante de tiempo: {tau:.6f} s")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(tiempo, carga, label="Carga", linewidth=2, color="forestgreen")
    ax.plot(tiempo, descarga, label="Descarga", linewidth=2, color="darkorange")
    ax.axvline(tau, linestyle="--", color="gray", label=f"τ = {tau:.4g} s")
    ax.set_title("Carga y descarga de un circuito RC")
    ax.set_xlabel("Tiempo [s]")
    ax.set_ylabel("Voltaje del capacitor [V]")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
