from funciones import *
titulos = leer_titulos('./data/GH.csv')
print(titulos[:20])


print(cuenta_titulos(titulos))

print(calcula_total_titulos(titulos))

print(pelicula_mejor_valorada(titulos))

print(mejores_valoradas(titulos))

print(titulo_puntuacion(titulos))

