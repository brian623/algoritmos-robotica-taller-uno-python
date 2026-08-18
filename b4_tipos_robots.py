"""Punto B.4: informa las articulaciones del robot seleccionado."""


ROBOTS = {
    "1": {
        "nombre": "Cilíndrico",
        "articulaciones": "RPP",
        "descripcion": "1 rotacional y 2 prismáticas",
    },
    "2": {
        "nombre": "Cartesiano",
        "articulaciones": "PPP",
        "descripcion": "3 prismáticas",
    },
    "3": {
        "nombre": "Esférico",
        "articulaciones": "RRP",
        "descripcion": "2 rotacionales y 1 prismática",
    },
}


def seleccionar_robot() -> dict[str, str]:
    """Solicita una opción hasta que corresponda a un robot disponible."""
    while True:
        print("\n1. Robot cilíndrico")
        print("2. Robot cartesiano")
        print("3. Robot esférico")
        opcion = input("Seleccione un robot: ").strip()
        if opcion in ROBOTS:
            return ROBOTS[opcion]
        print("Opción no válida. Seleccione un número del 1 al 3.")


def main() -> None:
    """Muestra el tipo y el número de articulaciones del robot elegido."""
    print("Clasificación de robots por articulaciones")
    robot = seleccionar_robot()

    print(f"\nRobot seleccionado: {robot['nombre']}")
    print("Número de articulaciones: 3")
    print(f"Configuración: {robot['articulaciones']}")
    print(f"Tipo de articulaciones: {robot['descripcion']}")


if __name__ == "__main__":
    main()
