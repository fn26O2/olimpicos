"""
Código común del proyecto: carga de datos y estilo de gráficos.
Los dos notebooks empiezan con:  from comun import *
En la entrega final, copiad este código en la primera celda de código
(el notebook tiene que ser autocontenido).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

DATA = Path(__file__).resolve().parent / "data"

# --- Carga -----------------------------------------------------------------
df_atletas = pd.read_csv(DATA / "atletas.csv")    # 1 fila por atleta (ID único)
df_medallas = pd.read_csv(DATA / "medallas.csv")  # 1 fila por atleta y prueba

# --- Tabla combinada -------------------------------------------------------
# Relación 1:N por ID. Medal = NaN -> participó sin medalla.
df = df_medallas.merge(df_atletas, on="ID", how="left")
df["TieneMedalla"] = df["Medal"].notna()
df["Decada"] = (df["Year"] // 10) * 10

# --- Estilo común de gráficos ------------------------------------------------
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["figure.figsize"] = (10, 5)
COLORES_TEMPORADA = {"Summer": "#E07B39", "Winter": "#3A7CA5"}
COLORES_MEDALLA = {"Gold": "#D4AF37", "Silver": "#A8A9AD", "Bronze": "#CD7F32"}
