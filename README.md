# Análisis de los Juegos Olímpicos con Python y Pandas

Trabajo de **Python para Ciencia de Datos** (Máster F.P. en IA & Big Data Analytics, UPV, 2026-2027).

**Autores:** Álvaro Tébar Folch y Pablo Sánchez-Migallón Quevedo

**Estado:** terminado y corregido. Pendiente de entregar en PoliformaT.

## Contenido

```
data/
├── Juegos_Olimpicos_Tebar_y_Sanchez.ipynb   notebook de entrega (autocontenido)
├── atletas.csv                              1 fila por atleta
└── medallas.csv                             1 fila por atleta y prueba
requirements.txt
README.md
```

El notebook lee los CSV desde su misma carpeta, así que los tres archivos tienen que estar juntos.

## Cómo ejecutarlo

```bash
conda create -n olimpicos python=3.12 -y
conda activate olimpicos
pip install -r requirements.txt ipykernel
```

Abre el notebook en VS Code, elige el kernel `olimpicos` (Select Kernel) y pulsa **Restart** y después **Run All**.

## De qué trata

Analizamos los Juegos Olímpicos de 1896 a 2016 con dos tablas que se unen por el `ID` del atleta.

- **0. Exploración y limpieza.** Tipos de datos, valores ausentes y duplicados. Excluimos Art Competitions y calculamos la edad de cada atleta en cada edición, porque la tabla solo guarda la edad del debut.
- **Reto 1. Relación entre las tablas.** Listado de ejemplo, preguntas que necesitan las dos tablas, participaciones por país y la función `resumen_participacion`.
- **Reto 2. Perfil de los atletas.** Edad por temporada y por país, reparto por sexo, físico de las mujeres en los deportes con más mujeres y la función `extremos_atletas`.
- **Reto 3. Medallas y rendimiento.** Mapa de calor país × deporte, top 10, evolución por décadas, físico y medallas en remo y la función `ranking_paises_medallas`.
- **Reto 4. Participación de las mujeres.** Evolución, diferencias entre países y deportes, pruebas femeninas y la función `anio_umbral_mujeres`.

## Criterios usados

- **Medallas de equipo:** cuando comparamos países se cuentan una vez por prueba, como en el medallero oficial. Cuando analizamos atletas, una por atleta.
- **País:** columna `NOC`, no `Team`.
- **Participación:** un atleta en una edición (`Games`), no cada prueba.
- **Años consecutivos:** la siguiente edición celebrada de la misma temporada, no siempre +4 años.
- **Edad:** edad en la edición = edad en el debut + (año de la edición − año del debut).

## Historial de correcciones (13/11/2026)

- `extremos_atletas(df_atletas)` y `ranking_paises_medallas(df_medallas, k)` se pueden llamar como en el enunciado (tablas limpias como valor por defecto).
- 0.6: comprobación de que la edad de la tabla es la del debut, con Phelps, Yao Ming, Bjørndalen y Bolt.
- Reto 2: nota sobre el atleta de más edad según la edición (Oscar Swahn, 72 años en 1920). Corregidos el comentario de las cajas de peso (2.4) y el umbral de peso.
- Reto 3: la URSS supera a EE. UU. desde los años 50; mención a FRG en 3.2.
- Retoques de texto en 0.4 y 0.5, una limitación más en el Reto 4 e índice con enlaces.
- Eliminados los notebooks de borrador y `comun.py`.

## Entrega

- [ ] Uno de los dos sube el `.ipynb` a la Tarea de PoliformaT.
- [ ] Nombres completos de los dos en el editor de la Tarea (ya están en la primera celda del notebook).
