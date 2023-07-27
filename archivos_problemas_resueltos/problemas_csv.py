#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")
#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(df["edad"][0])

#reemplazando los datos reyes por musico de la columna apellidos
df['apellido'].replace("reyes","musico", inplace=True)

#eliminando las filas con datos vacios
df = df.dropna() # si deseo eliminar columnas vacias es: df = df.dropna(axis=1)
#print(df)

#aliminando filas repetidas
df = df.drop_duplicates()
#print(df)
#creando un CSV con el dataframe resultante(limpio)
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")
print(df)