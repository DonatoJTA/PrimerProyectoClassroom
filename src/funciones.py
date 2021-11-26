from collections import namedtuple
import csv
from datetime import datetime
from typing import TypeVar

Titulos=namedtuple('type','title,director,cast,country,date_added,release_year,rating,duration,listed_in,description,show_id'
)
def leer_titulos(titulos):
    lista=[]
    cont = 0
    with open(titulos, encoding= 'utf-8') as f:
        lector= csv.readesr(f,delimiter =",")
        next(lector)
        for  e in lector:
            type=str(e[1])
            title= str(e[2])
            director=str(e[3])
            cast=str(e[4])
            country=str(e[5])
            date_added=int(e[6])
            release_year=int(e[7])
            rating=int(e[8])
            duration=float(e[9])
            listed_in=str(e[10])
            description=str(e[11])
            show_id=int(e[0])
            if type == "Movie" : 
                return print("Pelicula")
            else: print("Show de television")
            lista.append(titulos(title,director,cast,country,date_added,release_year,rating,duration,listed_in,description,type,show_id
))
        cont +=1
    return lista
#2#   
def cuenta_titulos(titulos):  
    titulos= []
    conj = set(titulo.title for titulo in titulos)
    return len(conj)
#3#
def calcula_total_titulos(titulos):
    cantidad_titulos=sum(c.title for c in titulos)
    return cantidad_titulos
#4-5#
def pelicula_mejor_valorada(titulos):
    dicc = mejores_valoradas(titulos)
    res = max(dicc.items(), key=lambda x:x[1])
    return res[0]   
#6#
def mejores_valoradas(titulos):
    titulos=[]
    with open(titulos, encoding= 'utf-8') as f:
        lector= csv.reader(f,delimiter =",")
        next(lector)
        for  e in lector:
            title= str(e[2])
            rating=int(e[8])
            if rating > 9:
                return title
#7#
def titulo_puntuacion(titulos):
    res = []
    for titulo in titulos:
        clave=titulo.rating
        if clave not in res:
            res[clave]= set(titulo.rating)
        else:
            res[clave].add(titulo.rating) 
    return res 
    

