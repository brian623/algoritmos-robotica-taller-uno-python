"""Punto C.5: dibuja con trazos los nombres de los integrantes."""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import PathPatch
from matplotlib.transforms import Affine2D
from matplotlib.textpath import TextPath


NOMBRES_INTEGRANTES = ["BRIAN"]


def crear_trazado_nombre(nombre: str, desplazamiento_y: float) -> TextPath:
    """Convierte un nombre en un trazado compuesto por líneas y curvas."""
    fuente = FontProperties(family="DejaVu Sans", weight="bold")
    trazado = TextPath((0, 0), nombre.upper(), size=1, prop=fuente)
    return trazado.transformed(Affine2D().scale(2.0).translate(0, desplazamiento_y))


def main() -> None:
    """Dibuja en 2D todos los nombres configurados en la lista."""
    if not NOMBRES_INTEGRANTES:
        raise ValueError("Debe agregar al menos un nombre a NOMBRES_INTEGRANTES.")

    fig, ax = plt.subplots(figsize=(10, 2.5 * len(NOMBRES_INTEGRANTES)))
    limites = []

    for indice, nombre in enumerate(NOMBRES_INTEGRANTES):
        trazado = crear_trazado_nombre(nombre, desplazamiento_y=-3.0 * indice)
        parche = PathPatch(
            trazado,
            facecolor="none",
            edgecolor=plt.cm.tab10(indice % 10),
            linewidth=2,
        )
        ax.add_patch(parche)
        limites.append(trazado.get_extents())

    ancho_maximo = max(limite.xmax for limite in limites)
    y_minimo = min(limite.ymin for limite in limites)
    y_maximo = max(limite.ymax for limite in limites)
    ax.set_xlim(-0.5, ancho_maximo + 0.5)
    ax.set_ylim(y_minimo - 0.5, y_maximo + 0.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Integrantes del grupo")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
