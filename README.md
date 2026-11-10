# Análisis de los Juegos Olímpicos con Python y Pandas

Trabajo de **Python para Ciencia de Datos** (Máster F.P. en IA & Big Data Analytics, UPV, 2026-2027).
Autores: Álvaro y Pablo.

## Estructura

```
├── data/
│   ├── atletas.csv          1 fila por atleta (ID único)
│   └── medallas.csv         1 fila por atleta y prueba (Medal vacío = sin medalla)
├── comun.py                 carga de datos, merge y estilo de gráficos (lo importan todos)
├── reto1_reto2.ipynb        Álvaro
├── reto3_reto4.ipynb        Pablo
├── entrega_final.ipynb      se monta al final copiando celdas
└── requirements.txt
```

Cada notebook ya tiene todos los enunciados colocados. Solo hay que rellenar las celdas `TODO`.
Empezad siempre con `from comun import *`, que os da `df_atletas`, `df_medallas` y `df` (las dos tablas unidas por `ID`, con las columnas extra `TieneMedalla` y `Decada`).

## Reparto

| Quién | Qué |
|---|---|
| Juntos | Decidir los criterios de abajo y la idea del Reto 4 |
| Álvaro | Reto 1 + Reto 2 (la función del R2 usa la del R1) |
| Pablo | Reto 3 + funciones y gráficas del Reto 4 |
| Álvaro | Conclusión y limitaciones del Reto 4 (al acabar el R2) |
| Juntos | Montar `entrega_final.ipynb`, Restart & Run All, repaso visual |

## Cómo trabajar con Git

1. **Nunca editéis el notebook del otro.** Así no hay conflictos.
2. `git pull` antes de empezar y `git commit` + `git push` al acabar.
3. Antes de cada commit: *Kernel → Restart & Clear Output* (el repo no se llena de imágenes).
4. Si cambiáis `comun.py`, avisad al otro: afecta a los dos.

## Criterios a decidir juntos

- **País:** usar `NOC`, no `Team` (que tiene valores como "United States-1").
- **Participaciones:** contar `Games` únicos por atleta, no filas.
- **Medallas por equipo:** un oro de baloncesto son ~12 filas. ¿Contamos por atleta o por prueba
  (eliminando duplicados por `Games` + `Event` + `NOC` + `Medal`)? Decisión: ______
- **Intervalos consecutivos:** "siguiente edición de la misma temporada", no `+4` a secas
  (Invierno 1992 → 1994, Juegos de 1906, sin Juegos en 1940/1944). Formato `"2000-2016"` con guion normal.
- **Edad:** en `atletas.csv` hay una sola edad por atleta, no una por edición. Comentarlo en el R2.
- **Décadas:** `Year // 10 * 10` (ya está en la columna `Decada`).

## Entrega

- Un único notebook **autocontenido**: en `entrega_final.ipynb` sustituir el `from comun import *` por el código de `comun.py`.
- Nombres completos de los dos en la **primera celda** y en el editor de la Tarea.
- **Solo uno** lo sube a PoliformaT.
