"""Punto A.1: operaciones básicas entre dos vectores inicializados."""

import numpy as np


def main() -> None:
    """Calcula y muestra las operaciones solicitadas entre dos vectores 3D."""
    vector_a = np.array([2.0, 4.0, 6.0])
    vector_b = np.array([1.0, 2.0, 4.0])

    suma = vector_a + vector_b
    resta = vector_a - vector_b
    producto_punto = np.dot(vector_a, vector_b)
    producto_cruz = np.cross(vector_a, vector_b)

    if np.any(vector_b == 0):
        raise ValueError("No es posible dividir entre un componente igual a cero.")

    division = vector_a / vector_b

    print(f"Vector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Producto punto: {producto_punto}")
    print(f"Producto cruz: {producto_cruz}")
    print(f"División elemento a elemento: {division}")


if __name__ == "__main__":
    main()
