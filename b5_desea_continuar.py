"""Punto B.5: repite una pregunta hasta que el usuario responda No."""


def desea_continuar() -> bool:
    """Devuelve True para Sí y False para No; rechaza otras respuestas."""
    while True:
        respuesta = input("¿Desea continuar Sí/No?: ").strip().casefold()
        if respuesta in {"s", "si", "sí"}:
            return True
        if respuesta in {"n", "no"}:
            return False
        print("Respuesta no válida. Escriba Sí o No.")


def main() -> None:
    """Mantiene activa la pregunta hasta recibir una respuesta negativa."""
    while desea_continuar():
        print("El programa continúa.")

    print("Programa finalizado.")


if __name__ == "__main__":
    main()
