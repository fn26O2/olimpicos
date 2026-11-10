# Análisis de los Juegos Olímpicos con Python y Pandas

Trabajo de **Python para Ciencia de Datos** (Máster F.P. en IA & Big Data Analytics, UPV, 2026-2027).
Autores: Álvaro y Pablo.

## De qué va el proyecto

Tenemos datos de todos los Juegos Olímpicos entre 1896 y 2016, repartidos en dos tablas:

- **`atletas.csv`**: unos 135.000 deportistas, con su nombre, sexo, edad, altura, peso y país.
- **`medallas.csv`**: unas 271.000 participaciones. Cada fila es un atleta compitiendo en una prueba concreta: en qué Juegos (año, Verano o Invierno), en qué deporte y si ganó oro, plata, bronce o nada.

Las dos tablas se unen por la columna `ID` del atleta. El trabajo consiste en cruzarlas con pandas, hacer gráficas y explicar lo que vemos. Se entrega **un único notebook** bien presentado, con el enunciado de cada tarea, el código, las gráficas y nuestros comentarios.

## De qué va cada reto

### Reto 1 · Entender los datos (Álvaro)
Es la toma de contacto. Explicamos qué información tiene cada tabla y por qué necesitamos las dos. Sacamos un ejemplo de unos cuantos atletas con los años en que compitieron y lo que ganaron, y pensamos tres preguntas que solo se pueden contestar juntando ambas tablas. Además hay que hacer una gráfica de barras con los 10 países que más han participado, separando Verano e Invierno.

La función de este reto, `resumen_participacion`, recibe un atleta y devuelve sus años de participación agrupados en tramos seguidos. Por ejemplo, Phelps compitió en 2000, 2004, 2008, 2012 y 2016, así que su resultado es "5 participaciones, de 2000 a 2016".

### Reto 2 · Cómo son los atletas (Álvaro)
Aquí miramos el perfil físico. Comparamos la edad media en Verano y en Invierno, vemos cómo se reparten las edades en los 5 países con más atletas, calculamos qué porcentaje son hombres y mujeres en cada tipo de Juegos y estudiamos la altura y el peso de las mujeres en los deportes donde hay más mujeres que hombres.

La función de este reto, `extremos_atletas`, busca los récords: el atleta más joven, el más mayor, el más alto, el más bajo, el más ligero y el más pesado. Antes hay que descartar datos imposibles (alguien de 40 cm o de 400 kg) y explicar con qué límites lo hemos hecho.

### Reto 3 · Medallas y rendimiento (Pablo)
Es el reto del medallero. Hay que hacer un mapa de calor de países frente a deportes coloreado según las medallas, sacar los 10 países con más medallas y el deporte en el que más ha ganado cada uno, y ver cómo han evolucionado los 5 primeros década a década. Por último, se elige un deporte y se analiza si la altura o el peso influyen en ganar medalla según el país.

La función de este reto, `ranking_paises_medallas`, hace el medallero clásico: primero ordena por oros, si hay empate por platas y después por bronces. Si siguen empatados, va antes el país que ganó su primera medalla hace más tiempo, y como último recurso se ordena alfabéticamente.

### Reto 4 · Reto libre (Pablo, con conclusión de Álvaro)
Nos inventamos nosotros una pregunta sobre los datos y la resolvemos igual que las anteriores: 4 tareas, al menos una gráfica (justificando por qué ese tipo), una función documentada y una conclusión final que incluya las limitaciones de los datos. Pablo propone la pregunta.

Algunas ideas: "¿Ganan más medallas los países cuando son anfitriones?", "¿Cómo ha crecido la participación femenina?" o "¿A qué edad se gana más en cada deporte?".

## Criterios acordados

Aplican a los dos notebooks.

- **Medallas por equipo: se cuentan POR PRUEBA, como en el medallero oficial.** Un oro de waterpolo aparece en los datos como 13 filas (una por jugador), pero cuenta como **1** medalla para el país. Para contar medallas de países se usa siempre:
  ```python
  medallas_pais = (df[df["TieneMedalla"]]
                   .drop_duplicates(subset=["Games", "Event", "NOC", "Medal"]))
  ```
  Cuando se analizan atletas individuales (por ejemplo, la altura de los medallistas), sí se usa cada fila.
- **País:** usar la columna `NOC` (código de país, por ejemplo `ESP`), no `Team`, que tiene valores raros como "United States-1".
- **Participaciones de un atleta:** contar los `Games` distintos en los que aparece, no las filas, porque un atleta puede competir en varias pruebas en los mismos Juegos.
- **Años consecutivos:** se considera consecutiva la siguiente edición de la misma temporada, no simplemente sumar 4. Los de Invierno pasaron de 1992 a 1994, hubo unos Juegos en 1906 y no se celebraron en 1940 ni 1944. Los intervalos se escriben con guion normal: `"2000-2016"`.
- **Edad:** en `atletas.csv` cada atleta tiene una sola edad, no una por edición. Hay que comentarlo en el Reto 2.
- **Décadas:** `Year // 10 * 10`. Ya está calculado en la columna `Decada`.

## Estructura del repo

```
├── data/
│   ├── atletas.csv
│   └── medallas.csv
├── comun.py                 carga los datos, une las tablas y define el estilo de gráficos
├── reto1_reto2.ipynb        Álvaro
├── reto3_reto4.ipynb        Pablo
├── entrega_final.ipynb      se monta al final copiando las celdas de los dos
└── requirements.txt
```

Cada notebook ya tiene todos los enunciados colocados, solo hay que rellenar las celdas `TODO`. Todos empiezan con `from comun import *`, que carga:

- `df_atletas`: la tabla de atletas.
- `df_medallas`: la tabla de medallas.
- `df`: las dos tablas unidas, con las columnas extra `TieneMedalla` (True/False) y `Decada`.

## Primeros pasos (Pablo)

```bash
git clone https://github.com/fn26O2/olimpicos.git
cd olimpicos
pip install -r requirements.txt
jupyter notebook
```

Después abre `reto3_reto4.ipynb`.

## Tareas

Marcad cada casilla cambiando `[ ]` por `[x]` y haced push.

### Álvaro (`reto1_reto2.ipynb`)
- [ ] Función `resumen_participacion` (pasa el test de Phelps). **Va primero, porque el Reto 2 la necesita.**
- [ ] 1.1 Explicación de las tablas
- [ ] 1.2 Listado de ejemplo
- [ ] 1.3 Tres preguntas
- [ ] 1.4 Barras apiladas Top-10 Verano/Invierno
- [ ] 2.1 Edad media Verano vs Invierno
- [ ] 2.2 FacetGrid de edades (Top-5 países)
- [ ] 2.3 % Hombre/Mujer × Verano/Invierno
- [ ] 2.4 Altura/peso de mujeres en 5 deportes
- [ ] Función `extremos_atletas` con umbrales justificados
- [ ] R4: conclusión y limitaciones

### Pablo (`reto3_reto4.ipynb`)
- [ ] 3.1 Mapa de calor país × deporte
- [ ] 3.2 Top-10 países y su deporte estrella
- [ ] 3.3 Evolución por décadas (Top-5)
- [ ] 3.4 Altura/peso vs probabilidad de medalla
- [ ] Función `ranking_paises_medallas`
- [ ] R4: proponer la pregunta, las 4 tareas, las gráficas y la función documentada

### Al final, juntos
- [ ] Copiar las celdas de los dos notebooks a `entrega_final.ipynb`
- [ ] Sustituir `from comun import *` por el código de `comun.py` (el notebook debe ser autocontenido)
- [ ] Poner los nombres completos en la primera celda
- [ ] Restart & Run All sin errores
- [ ] Repaso visual (títulos, comentarios, gráficas legibles)
- [ ] Uno de los dos lo sube a PoliformaT, con los dos nombres también en el editor de la Tarea

## Cómo trabajar con Git

1. **Nunca editéis el notebook del otro.** Así no hay conflictos.
2. `git pull` antes de empezar, y `git add .`, `git commit -m "..."` y `git push` al acabar.
3. Antes de cada commit: *Kernel → Restart & Clear Output*, para que el repo no se llene de imágenes.
4. Si cambiáis `comun.py`, avisad al otro, porque afecta a los dos.
