# Guía de sustentación - Puntos A.2 a A.6

## A.2 - Operaciones con matrices

El programa crea dos matrices de 3 x 3 con `np.array`. La suma, la resta y la
división se realizan elemento a elemento: cada posición de la matriz A opera con
la misma posición de la matriz B.

El operador `@` realiza el producto matricial. Para obtener cada elemento del
resultado se multiplica una fila de A por una columna de B y se suman esos
productos.

El producto cruz no está definido directamente entre matrices como una única
operación. Como cada fila tiene tres componentes, el programa interpreta cada
fila como un vector 3D y usa `np.cross(..., axis=1)` para calcular el producto
cruz entre las filas correspondientes.

Antes de dividir se comprueba con `np.any(matriz_b == 0)` que la matriz B no
contenga ceros. Esto evita una división indefinida.

Punto clave para explicar: `*` representaría multiplicación elemento a elemento,
mientras que `@` representa el producto matricial convencional.

## A.3 - Conversión de coordenadas

Se parte de un punto rectangular `(x, y, z)`. El programa separa las conversiones
en dos funciones para que cada una tenga una responsabilidad concreta.

Para coordenadas cilíndricas se usan:

```text
r = sqrt(x² + y²)
theta = atan2(y, x)
z = z
```

Para coordenadas esféricas se usan:

```text
rho = sqrt(x² + y² + z²)
theta = atan2(y, x)
phi = acos(z / rho)
```

`theta` es el azimut medido en el plano XY y `phi` es el ángulo polar medido
desde el eje Z positivo. `atan2` se prefiere sobre `atan(y/x)` porque identifica
correctamente el cuadrante y funciona cuando `x` es cero. Las funciones
trigonométricas trabajan en radianes; `degrees` se usa solo para mostrar los
ángulos en grados.

El caso del origen se controla porque allí `rho` es cero y no se puede calcular
`z/rho`.

## A.4 - Resistencia de una PT100

Una PT100 es una RTD de platino cuya resistencia nominal es `R0 = 100 ohmios` a
0 °C. El programa usa la ecuación de Callendar-Van Dusen y sus coeficientes
estándar:

```text
A = 3.9083 x 10⁻³
B = -5.775 x 10⁻⁷
C = -4.183 x 10⁻¹²
```

Para temperaturas mayores o iguales a 0 °C:

```text
R(T) = R0 (1 + A*T + B*T²)
```

Para temperaturas menores que 0 °C se agrega el término que corrige la no
linealidad a bajas temperaturas:

```text
R(T) = R0 [1 + A*T + B*T² + C*(T - 100)*T³]
```

La función valida el intervalo de -200 °C a 850 °C. Con `T = -50 °C`, el
resultado es aproximadamente `80.3063 ohmios`. También se puede comprobar que a
0 °C el resultado es exactamente 100 ohmios.

## A.5 - Matrices de rotación

Hay una función para cada eje. Todas reciben un ángulo en grados y devuelven una
matriz NumPy de 3 x 3. `radians` convierte el dato porque `sin` y `cos` esperan
radianes.

Las matrices emplean la convención de rotaciones activas y la regla de la mano
derecha. Cada matriz mantiene sin cambio la coordenada correspondiente a su eje:

- La rotación en X conserva la coordenada X y mezcla Y con Z.
- La rotación en Y conserva la coordenada Y y mezcla X con Z.
- La rotación en Z conserva la coordenada Z y mezcla X con Y.

Las matrices de rotación son ortogonales. Por eso su inversa es igual a su
transpuesta y su determinante es 1. Estas propiedades permiten verificar que no
deforman ni cambian la longitud de los vectores: solo los orientan.

## A.6 - Fuerzas de un cilindro neumático

La relación fundamental es:

```text
Fuerza = Presión * Área
```

En el avance, la presión actúa sobre toda el área circular del pistón:

```text
A_avance = pi * D² / 4
```

En el retroceso, el vástago ocupa parte de esa superficie. La presión actúa
sobre un área anular menor:

```text
A_retroceso = pi * (D² - d²) / 4
```

`D` es el diámetro del pistón y `d` el del vástago. El programa convierte bar a
pascales y milímetros a metros antes de operar, de modo que el resultado queda
en newtons.

Con 6 bar, un pistón de 50 mm y un vástago de 20 mm se obtienen aproximadamente
`1178.10 N` al avanzar y `989.60 N` al retroceder. La fuerza de retroceso es
menor debido al área ocupada por el vástago.

Estas son fuerzas teóricas. En un cilindro real se reducen por rozamiento,
pérdidas de presión y otras condiciones de operación.
