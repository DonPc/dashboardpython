import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from streamlit.source_util import page_icon_and_name

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración general
sns.set(style="whitegrid")
st.set_page_config(page_title="Dashboard Logístico", layout="wide")

# Cargar datos
df = pd.read_csv('data/Tiempos_Log_sticos_de_cada_viaje_de_veh_culos_de_carga_20250609.csv')

# Preprocesamiento
df = df.dropna(subset=["PRODUCTO", "HORAS_VIAJE"])
df["HORAS_VIAJE"] = pd.to_numeric(df["HORAS_VIAJE"], errors="coerce")

# Título
st.title("📦 Dashboard de Tiempos Logísticos en Colombia")

# Sidebar de selección
grafico = st.sidebar.selectbox("Selecciona un gráfico", [
    "Histograma de Horas de Viaje por Producto",
    "Boxplot de Horas de Espera Descargue",
    "Dispersión: Espera Cargue vs Espera Descargue",
    "Conteo de Productos",
    "Distribución Valor Pagado",
    "Línea de Tiempo Valor Pagado",
    "Mapa de Calor: Valor Pagado vs Horas de Viaje",
    "Promedio de Horas de Viaje por Tipo de Cargue",
    "Boxplot General de Variables",
    "Comparación KDE: Valor Pagado, Horas y Cantidad",
    "Boxplot Valor Pagado según Cargue",
    "Dispersión: Horas de Viaje vs Valor Pagado"
])

# Mostrar gráficos según selección
if grafico == "Histograma de Horas de Viaje por Producto":
    top_productos = df['PRODUCTO'].value_counts().nlargest(4).index
    df_filtrado = df[df['PRODUCTO'].isin(top_productos)]
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_filtrado, x='HORAS_VIAJE', hue='PRODUCTO', bins=30, kde=True, element='step', stat='density')
    plt.title("Histograma de Horas de Viaje por Producto")
    st.pyplot(plt.gcf())

elif grafico == "Boxplot de Horas de Espera Descargue":
    plt.figure(figsize=(10, 4))
    sns.boxplot(x=df["HORAS_ESPERA_DESCARGUE"])
    plt.title("Boxplot de Horas de Espera Descargue")
    st.pyplot(plt.gcf())

elif grafico == "Dispersión: Espera Cargue vs Espera Descargue":
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df["HORAS_ESPERA_CARGUE"], y=df["HORAS_ESPERA_DESCARGUE"], alpha=0.5)
    plt.title("Relación entre Espera Cargue y Descargue")
    st.pyplot(plt.gcf())

elif grafico == "Conteo de Productos":
    plt.figure(figsize=(10, 6))
    sns.countplot(x="PRODUCTO", data=df, palette="viridis")
    plt.title("Cantidad de Productos")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

elif grafico == "Distribución Valor Pagado":
    plt.figure(figsize=(10, 6))
    sns.histplot(df["VALOR_PAGADO"], bins=20, kde=True, color='coral')
    plt.title("Distribución de Valor Pagado")
    st.pyplot(plt.gcf())

elif grafico == "Línea de Tiempo Valor Pagado":
    df["FECHASALIDACARGUE"] = pd.to_datetime(df["FECHASALIDACARGUE"], errors='coerce')
    df = df.dropna(subset=["FECHASALIDACARGUE"])
    df = df.sort_values("FECHASALIDACARGUE")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='FECHASALIDACARGUE', y='VALOR_PAGADO', marker='o')
    plt.xticks(rotation=45)
    plt.title("Valor Pagado a lo largo del tiempo")
    st.pyplot(plt.gcf())

elif grafico == "Mapa de Calor: Valor Pagado vs Horas de Viaje":
    plt.figure(figsize=(8, 6))
    plt.hist2d(df["VALOR_PAGADO"], df["HORAS_VIAJE"], bins=30, cmap='viridis')
    plt.colorbar()
    plt.title("Mapa de Calor: Valor Pagado vs Horas de Viaje")
    st.pyplot(plt.gcf())

elif grafico == "Promedio de Horas de Viaje por Tipo de Cargue":
    plt.figure(figsize=(10, 6))
    sns.barplot(x="CARGUE", y="HORAS_VIAJE", data=df, ci="sd", palette="coolwarm")
    plt.title("Horas de Viaje Promedio por Tipo de Cargue")
    plt.xticks(rotation=45)
    st.pyplot(pl)
