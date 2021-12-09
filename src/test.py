from funciones import *
registros = leer_titulos('./PrimerProyectoClassroom/data/netflix_titles.csv')
# 

print(registros[:20])



print(cuenta_titulos(registros))

print(calcula_total_titulos(registros))

print(pelicula_mejor_valorada(registros))

print(mejores_valoradas(registros))

print(titulo_puntuacion(registros))

