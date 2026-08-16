"""Punto A.2: operaciones entre dos matrices previamente inicializadas."""

import numpy as np


def main() -> None:
    """Calcula y muestra las operaciones solicitadas entre matrices de 3 x 3."""
    matriz_a = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
        ]
    )
    matriz_b = np.array(
        [
            [9.0, 8.0, 7.0],
            [6.0, 5.0, 4.0],
            [3.0, 2.0, 1.0],
        ]
    )

    if np.any(matriz_b == 0):
        raise ValueError("La matriz B no puede contener ceros para la división.")

    suma = matriz_a + matriz_b
    resta = matriz_a - matriz_b
    producto_matricial = matriz_a @ matriz_b
    producto_cruz_por_filas = np.cross(matriz_a, matriz_b, axis=1)
    division = matriz_a / matriz_b

    print(f"Matriz A:\n{matriz_a}")
    print(f"\nMatriz B:\n{matriz_b}")
    print(f"\nSuma:\n{suma}")
    print(f"\nResta:\n{resta}")
    print(f"\nProducto matricial (A @ B):\n{producto_matricial}")
    print(f"\nProducto cruz entre filas correspondientes:\n{producto_cruz_por_filas}")
    print(f"\nDivisión elemento a elemento:\n{division}")


if __name__ == "__main__":
    main()
