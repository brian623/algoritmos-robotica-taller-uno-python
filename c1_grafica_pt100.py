"""Punto C.1: grafica una PT100 entre -200 °C y 200 °C."""

import matplotlib.pyplot as plt
import numpy as np

from a4_resistencia_pt100 import resistencia_pt100


def generar_curva_pt100() -> tuple[np.ndarray, np.ndarray]:
    """Devuelve temperaturas y resistencias para la curva de la PT100."""
    temperaturas = np.linspace(-200, 200, 401)
    resistencias = np.array([resistencia_pt100(t) for t in temperaturas])
    return temperaturas, resistencias


def main() -> None:
    """Construye y muestra la gráfica de resistencia contra temperatura."""
    temperaturas, resistencias = generar_curva_pt100()

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(temperaturas, resistencias, color="crimson", linewidth=2)
    ax.scatter([0], [100], color="navy", zorder=3, label="100 Ω a 0 °C")
    ax.set_title("Comportamiento de un sensor PT100")
    ax.set_xlabel("Temperatura [°C]")
    ax.set_ylabel("Resistencia [Ω]")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
