import pandas as pd
#print(type(pd))
#df = pd.read_csv("archivos\\datos.csv", names=["name","lastname","age"])
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo los datos de la columna nombre
#nombres = df["nombre"]

df_ordenado_ascendente = df.sort_values("edad")
#ordenandolo de forma desendente
df_ordenado_desendente = df.sort_values("edad", ascending=False)
#print(df_ordenado_desendente)

#concatenando los dos data frames
df_concatenado = pd.concat([df,df2])
#print(df_concatenado)

#accediendo a las primeras 2 filas con head
primer_fila = df.head(2)

#accediendo a las ultimas 2 filas con tail
ultimas_filas = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape()
filas_totales,columnas_totales = df.shape

#obtener data estadistica del data frame
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2, "edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_loc_2 = df.iloc[2, 2]

#accediendo a todas las filas de una columna con loc
apellidos = df.loc[:,"apellido"]

#accediendo a todas las filas de una columna con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a las filas con edad mayor que 30
mayor_que_25 = df.loc[df["edad"]>25,:]

print(mayor_que_25)

# cadena = "0102373765"
# print(cadena[2:7]) #slide sing
