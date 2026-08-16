"""Punto A.5: matrices de rotación alrededor de los ejes X, Y y Z."""

from math import cos, radians, sin

import numpy as np


def rotacion_x(angulo_grados: float) -> np.ndarray:
    """Devuelve la matriz de rotación en X para un ángulo en grados."""
    angulo = radians(angulo_grados)
    return np.array(
        [
            [1, 0, 0],
            [0, cos(angulo), -sin(angulo)],
            [0, sin(angulo), cos(angulo)],
        ]
    )


def rotacion_y(angulo_grados: float) -> np.ndarray:
    """Devuelve la matriz de rotación en Y para un ángulo en grados."""
    angulo = radians(angulo_grados)
    return np.array(
        [
            [cos(angulo), 0, sin(angulo)],
            [0, 1, 0],
            [-sin(angulo), 0, cos(angulo)],
        ]
    )


def rotacion_z(angulo_grados: float) -> np.ndarray:
    """Devuelve la matriz de rotación en Z para un ángulo en grados."""
    angulo = radians(angulo_grados)
    return np.array(
        [
            [cos(angulo), -sin(angulo), 0],
            [sin(angulo), cos(angulo), 0],
            [0, 0, 1],
        ]
    )


def main() -> None:
    """Calcula las tres matrices para un ángulo previamente inicializado."""
    angulo = 30.0
    np.set_printoptions(precision=4, suppress=True)

    print(f"Ángulo de rotación: {angulo}°")
    print(f"\nRotación en X:\n{rotacion_x(angulo)}")
    print(f"\nRotación en Y:\n{rotacion_y(angulo)}")
    print(f"\nRotación en Z:\n{rotacion_z(angulo)}")


if __name__ == "__main__":
    main()
