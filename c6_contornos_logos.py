"""Punto C.6: obtiene coordenadas de contornos de dos logos automotrices."""

import cv2
import matplotlib.pyplot as plt
import numpy as np


def crear_logo_chevrolet() -> np.ndarray:
    """Crea una máscara binaria simplificada del emblema tipo corbatín."""
    imagen = np.zeros((300, 500), dtype=np.uint8)
    puntos = np.array(
        [[60, 120], [190, 120], [215, 90], [440, 90], [440, 180],
         [310, 180], [285, 210], [60, 210]],
        dtype=np.int32,
    )
    cv2.fillPoly(imagen, [puntos], 255)
    return imagen


def crear_logo_renault() -> np.ndarray:
    """Crea una máscara binaria simplificada de un emblema romboidal."""
    imagen = np.zeros((300, 500), dtype=np.uint8)
    rombo_exterior = np.array([[250, 35], [390, 150], [250, 265], [110, 150]])
    rombo_interior = np.array([[250, 90], [325, 150], [250, 210], [175, 150]])
    cv2.fillPoly(imagen, [rombo_exterior.astype(np.int32)], 255)
    cv2.fillPoly(imagen, [rombo_interior.astype(np.int32)], 0)
    return imagen


def extraer_contornos(imagen: np.ndarray) -> list[np.ndarray]:
    """Extrae cada contorno como una matriz de coordenadas (x, y)."""
    contornos, _ = cv2.findContours(imagen, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    return [contorno.reshape(-1, 2) for contorno in contornos]


def graficar_contornos(ax: plt.Axes, contornos: list[np.ndarray], titulo: str) -> None:
    """Dibuja en un eje las coordenadas de todos los contornos recibidos."""
    for indice, coordenadas in enumerate(contornos, start=1):
        x = coordenadas[:, 0]
        y = -coordenadas[:, 1]
        ax.plot(x, y, linewidth=2, label=f"Contorno {indice}")
    ax.set_title(titulo)
    ax.set_xlabel("Coordenada X [px]")
    ax.set_ylabel("Coordenada Y [px]")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.25)
    ax.legend()


def main() -> None:
    """Genera los logos, extrae sus coordenadas y grafica los contornos."""
    logos = {
        "Chevrolet - corbatín simplificado": crear_logo_chevrolet(),
        "Renault - rombo simplificado": crear_logo_renault(),
    }
    resultados = {nombre: extraer_contornos(imagen) for nombre, imagen in logos.items()}

    for nombre, contornos in resultados.items():
        cantidad_puntos = sum(len(contorno) for contorno in contornos)
        print(f"{nombre}: {len(contornos)} contorno(s), {cantidad_puntos} puntos")

    fig, ejes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, (nombre, contornos) in zip(ejes, resultados.items()):
        graficar_contornos(ax, contornos, nombre)
    fig.suptitle("Coordenadas de contornos de logos automotrices")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
