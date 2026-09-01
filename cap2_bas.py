#### 01/09/26
#### OBJ: REPLICAR CÓDIGOS DE HOML CAP2

import pandas as pd
import matplotlib.pyplot as plt

#### 00. CONFIGURACIÓN

## MURESTRA TODAS LAS COLUMNAS
pd.set_option("display.max_columns", None)
#pd.set_option("display.max_rows", None)

## NO HACE SALTO DE LINEA EN CMD
pd.set_option("display.width", None)

## TAMAÑO MAX COLUMNAS
pd.set_option("display.max_colwidth", 40)


# CARGA LA BASE DE DATOS
df = pd.read_csv("housing.csv")


#### 01. RECONOCIMIENTO

# MUESTRA LOS DATOS
print(df.head())
# MUESTRA LOS DATOS
print(df.info())
# MUESTRA LOS DATOS
print(df.describe())

# CUENTA TODOS LOS DATOS
#print(df.value_counts())

# CUENTA DATOS DEL ATRUBITO SOLICITAOD
print(df["ocean_proximity"].value_counts())


#### 02. VISUALIZACIÓN

# HISTOGRAMAS
plt.figure()
df.hist(bins=50, figsize=(20,15))
plt.title("Resumen")


# SOLO UN FEATURE
plt.figure()
df["median_house_value"].hist(bins=50, figsize=(20,15))
plt.title("FRECUENCIA DE VALORES")

# DENSIDAD DE LOS DATOS
plt.figure()
df.plot(kind="scatter", x="longitude", y="latitude", alpha=0.2)
plt.title("DENSIDAD DE DATOS")

# COLORMAT
plt.figure()
df.plot(    kind    ="scatter",
            x       ="longitude",
            y       ="latitude",
            alpha   =0.4,
            s       =df["population"]/100,
            label   ="population",
            figsize =(10,7),
            c       ="median_house_value",
            cmap=plt.get_cmap("jet"),
            colorbar=True,)
plt.legend()
plt.title("VALORES")

plt.show()