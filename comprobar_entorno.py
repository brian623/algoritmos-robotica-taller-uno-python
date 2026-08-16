"""Comprueba que las dependencias del taller estén disponibles."""

from importlib import import_module


DEPENDENCIAS = {
    "numpy": "Cálculo con vectores y matrices",
    "matplotlib": "Generación de gráficas",
    "scipy": "Análisis de sistemas y señales",
    "cv2": "Procesamiento de contornos de imágenes",
}


def main() -> None:
    """Importa cada dependencia y muestra el resultado de la comprobación."""
    errores: list[str] = []

    for modulo, uso in DEPENDENCIAS.items():
        try:
            paquete = import_module(modulo)
            version = getattr(paquete, "__version__", "versión no informada")
            print(f"[OK] {modulo} ({version}): {uso}")
        except ImportError:
            errores.append(modulo)
            print(f"[FALTA] {modulo}: {uso}")

    if errores:
        faltantes = ", ".join(errores)
        raise SystemExit(
            f"\nFaltan dependencias: {faltantes}. "
            "Ejecute: python -m pip install -r requirements.txt"
        )

    print("\nEl entorno está listo para desarrollar el taller.")


if __name__ == "__main__":
    main()
