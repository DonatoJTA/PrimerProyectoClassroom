from funciones import *

registros = leer_titulos('./PrimerProyectoClassroom/data/netflix_titles.csv') 

print(registros[:20])

print(cuenta_titulos(registros))

print(obtener_titulos(registros))

print(peliculas_de_mas_duracion(registros))

print(ordena_por_año(registros))

print(agrupa_por_año(registros))



