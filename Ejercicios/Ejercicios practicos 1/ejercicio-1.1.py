#promedio de durción

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
este_curso = 1.5

#crudo
crudo_promedio = 5
crudo_este = 3.5

# diferencias de duracion
diferencia_con_min = 100 - este_curso / otros_cursos_min * 100
diferencia_con_max = 100 - este_curso / otros_cursos_max * 100
diferencia_con_promedio = 100 - este_curso / otros_cursos_promedio * 100

#calculando porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 / crudo_promedio / 10
tiempo_vacio = 100 - este_curso * 1000 / crudo_este / 10

print(f"Este curso dura {diferencia_con_min}% menos que el más rápido")
print(f"Este curso dura {round(diferencia_con_max, 1)}% mas que el más lento")
print(f"Este curso dura {diferencia_con_promedio}% menos que el promedio")

#Mostarndo la cantida de espacios vacios que se remueven 
print(f"Un curso promedio elimina un {round(tiempo_vacio_promedio, 1)}% de tiempo vacio")
print(f"Este curso eliminó el {round(tiempo_vacio, 1)}% de tiempo vacio")

# mostrando diferencias si los otros cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio / este_curso * 10, 1)} horas de otros cursos")