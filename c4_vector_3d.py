"""Punto C.4: dibuja en 3D un vector ingresado por el usuario."""

import matplotlib.pyplot as plt


def leer_componente(nombre: str) -> float:
    """Solicita una componente numérica del vector."""
    while True:
        try:
            return float(input(f"Componente {nombre}: "))
        except ValueError:
            print("Entrada no válida. Ingrese un valor numérico.")


def main() -> None:
    """Solicita las coordenadas y representa el vector desde el origen."""
    print("Representación de un vector en un sistema XYZ")
    x = leer_componente("X")
    y = leer_componente("Y")
    z = leer_componente("Z")

    limite = max(abs(x), abs(y), abs(z), 1.0) * 1.2
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.quiver(0, 0, 0, x, y, z, color="crimson", linewidth=2, arrow_length_ratio=0.1)
    ax.scatter([x], [y], [z], color="navy")
    ax.text(x, y, z, f"  ({x:g}, {y:g}, {z:g})")
    ax.set_xlim(-limite, limite)
    ax.set_ylim(-limite, limite)
    ax.set_zlim(-limite, limite)
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    ax.set_title("Vector en el espacio tridimensional")
    ax.set_box_aspect((1, 1, 1))
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
