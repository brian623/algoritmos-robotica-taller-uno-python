# Taller 1 - Python

Ejercicios de la asignatura Electiva de Robótica de la Universidad ECCI.

Cada punto del taller se implementará en un archivo `.py` independiente. Los
ejercicios se agregarán y publicarán de manera incremental, uno por uno.

## Preparación del entorno

Se recomienda Python 3.11 o una versión posterior.

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python comprobar_entorno.py
```

### Linux o macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python comprobar_entorno.py
```

## Dependencias

- NumPy: operaciones con vectores y matrices.
- Matplotlib: gráficas 2D y 3D.
- SciPy: respuesta de sistemas y señales.
- OpenCV: extracción de contornos de imágenes.

El entorno virtual y los resultados generados localmente están excluidos del
repositorio mediante `.gitignore`.

## Ejercicios resueltos

- `a1_operaciones_vectores.py`: suma, resta, producto punto, producto cruz y
  división elemento a elemento de dos vectores tridimensionales.
- `a2_operaciones_matrices.py`: operaciones aritméticas, producto matricial y
  producto cruz por filas entre matrices de 3 x 3.
- `a3_conversion_coordenadas.py`: conversión de coordenadas rectangulares a
  cilíndricas y esféricas.
- `a4_resistencia_pt100.py`: resistencia de una PT100 mediante la ecuación de
  Callendar-Van Dusen.
- `a5_matrices_rotacion.py`: funciones que generan matrices de rotación en los
  ejes X, Y y Z.
- `a6_fuerza_cilindro.py`: fuerzas teóricas de avance y retroceso de un cilindro
  neumático de doble efecto.
- `b1_potencia_circuito.py`: potencia eléctrica a partir del voltaje y la
  corriente ingresados por teclado.
- `b2_numeros_aleatorios.py`: generación de enteros aleatorios dentro de un
  intervalo definido por el usuario.
- `b3_calculo_volumenes.py`: menú interactivo para calcular volúmenes de cuatro
  sólidos.
- `b4_tipos_robots.py`: identificación de las articulaciones de robots
  cilíndricos, cartesianos y esféricos.
- `b5_desea_continuar.py`: ciclo que pregunta al usuario si desea continuar.
- `c1_grafica_pt100.py`: curva de resistencia de una PT100 entre -200 °C y
  200 °C.
- `c2_sistema_segundo_orden.py`: respuesta al escalón y clasificación de un
  sistema de segundo orden.
- `c3_circuito_rc.py`: curvas de carga y descarga de un capacitor en un circuito
  RC.
- `c4_vector_3d.py`: representación de un vector ingresado por teclado en un
  sistema coordenado XYZ.
- `c5_nombres_integrantes.py`: nombres del grupo dibujados como trazados de
  líneas y curvas.
- `c6_contornos_logos.py`: extracción de vectores desde imágenes y reproducción
  de los logos de Chevrolet y Honda.
