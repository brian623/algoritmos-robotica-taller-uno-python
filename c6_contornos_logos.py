"""Punto C.6: extrae vectores de dos imágenes y reproduce sus logos."""

from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


CARPETA_MEDIA = Path(__file__).resolve().parent / "media"
LOGOS = {
    "Chevrolet": CARPETA_MEDIA / "logo_uno.png",
    "Honda": CARPETA_MEDIA / "logo_dos.png",
}


def crear_mascara(ruta_imagen: Path) -> np.ndarray:
    """Carga un logo y crea una máscara binaria de sus trazos oscuros."""
    if not ruta_imagen.is_file():
        raise FileNotFoundError(f"No existe la imagen: {ruta_imagen}")

    datos_imagen = np.fromfile(ruta_imagen, dtype=np.uint8)
    imagen = cv2.imdecode(datos_imagen, cv2.IMREAD_UNCHANGED)
    if imagen is None:
        raise FileNotFoundError(f"No se pudo leer la imagen: {ruta_imagen}")

    if imagen.ndim == 2:
        gris = imagen
    elif imagen.shape[2] == 4:
        gris = cv2.cvtColor(imagen[:, :, :3], cv2.COLOR_BGR2GRAY)
        canal_alfa = imagen[:, :, 3]
        gris[canal_alfa == 0] = 255
    else:
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    _, mascara = cv2.threshold(
        gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )
    return mascara


def extraer_vectores(mascara: np.ndarray) -> list[np.ndarray]:
    """Devuelve los contornos significativos como vectores de puntos (x, y)."""
    contornos, _ = cv2.findContours(
        mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE
    )
    vectores = [
        contorno.reshape(-1, 2)
        for contorno in contornos
        if cv2.contourArea(contorno) > 10
    ]
    return sorted(vectores, key=cv2.contourArea, reverse=True)


def reproducir_logo(
    ax: plt.Axes, vectores: list[np.ndarray], nombre: str
) -> None:
    """Reproduce un logo uniendo en orden los puntos de cada vector."""
    for vector in vectores:
        vector_cerrado = np.vstack([vector, vector[0]])
        x = vector_cerrado[:, 0]
        y = -vector_cerrado[:, 1]
        ax.plot(x, y, color="black", linewidth=2)

    ax.set_title(nombre)
    ax.set_xlabel("Coordenada X [px]")
    ax.set_ylabel("Coordenada Y [px]")
    ax.set_aspect("equal")
    ax.axis("off")


def main() -> None:
    """Carga las imágenes, extrae sus vectores y reproduce ambos logos."""
    resultados: dict[str, list[np.ndarray]] = {}

    for nombre, ruta in LOGOS.items():
        mascara = crear_mascara(ruta)
        vectores = extraer_vectores(mascara)
        if not vectores:
            raise ValueError(f"No se encontraron contornos en {ruta.name}.")
        resultados[nombre] = vectores

        total_puntos = sum(len(vector) for vector in vectores)
        print(
            f"{nombre} ({ruta.name}): "
            f"{len(vectores)} vector(es), {total_puntos} puntos"
        )

    fig, ejes = plt.subplots(1, 2, figsize=(12, 5))
    for ax, (nombre, vectores) in zip(ejes, resultados.items()):
        reproducir_logo(ax, vectores, nombre)

    fig.suptitle("Logos reproducidos a partir de sus vectores de contorno")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
