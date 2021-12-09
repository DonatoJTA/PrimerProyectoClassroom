from collections import namedtuple
import csv
from datetime import datetime
from typing import TypeVar

Peliculas=namedtuple('Peliculas','show_id,type_film,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description')
 
def leer_titulos(titulos):
    lista=[]
    with open(titulos, encoding= 'utf-8') as f:  #abrimos el fichero
        lector= csv.reader(f,delimiter =",") #definimos el 'lector' y como vamos a separar sus componentes
        next(lector) #hacemos que lea el siguientes
        for e in lector: #para cada posicion asignamos un valor 
            show_id=int(e[0])
            if str(e[1]) == "Movie" : 
                type_film = "Pelicula"
            else: 
                type_film = "Show de television"
            title= str(e[2])
            director=str(e[3])
            cast=str(e[4])
            country=str(e[5])
            date_added=str(e[6])
            release_year=int(e[7])
            rating=str(e[8])
            duration=str(e[9])
            listed_in=str(e[10])
            description=str(e[11])
            lista.append(Peliculas(show_id,type_film,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description))
            #añadimos a la lista la lectura
               
    return lista #devolvemos la lista

#2   

def cuenta_titulos(titulos):  
    c  = set(titulo.title for titulo in titulos) #decimos que c es cada titulo en titulos
    return len(c)     #contamos cada c y devolvemos el total

#3#
def obtener_titulos(titulos):
    return {c.title for c in titulos} #le decimos que nos devuelva cada titulo en el listado
#4-5#
def peliculas_de_mas_duracion(titulos):
    Max= max(b.duration for b in titulos) 
    return[b for b in titulos if b.duration == max] #te devuelve una lista de peliculas segun su duracion
    
#6
def ordena_por_año(titulos,n=3) :
    return sorted(((b.release_year,b.title) for b in titulos), reverse= True, key= lambda t: t[0])[:n]
    #usamos sorted para que nos devuelva un listado de elementos ordenados por key, la funcion lambda     
#7#
def agrupa_por_año(titulos):
    res= dict()
    for r in titulos:
        clave=r.release_year  #definimos clave, que nos ordena el diccionario segun esa propiedad
        if clave not in res:
            res[clave]=[r]     #establecemos las condiciones que la funcion debe cumplir, cambiando el res segun se cumpla una u otra
        else:
            res[clave].append(r)
    return res #devolvemos res

    

