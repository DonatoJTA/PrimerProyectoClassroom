[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5896993&assignment_repo_type=AssignmentRepo)
# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<21\>/\<22\>)
Autor/a: \<Donato Julian Trigueros Acosta\>   uvus:\<dontriaco\>

El data esta compuesto por un archivo que contiene el material del trabajo, el cual debemos organizar con una funcion


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<funciones.py\>**: Aqui hacemos una funcion que clasifique cada dato de la lista y los organice
  * **\<test.py\>**: En este modulo definimos una funcion con la cual le pedimos los 20 primeros titulos 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<data\>**:En esta parte encontramos los datos que vamos a usar en la funcion
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<12\> columnas, con la siguiente descripción:

* **\<columna 0>**: de tipo \<int\>, Es el id del contenido
* **\<columna 1>**: de tipo \<str\>, Tipo: pelicula o show de television
* **\<columna 2>**: de tipo \<str\>, Titulo de la obra
* **\<columna 3>**: de tipo \<str\>, Nombre del director
* **\<columna 4>**: de tipo \<str\>, Casting de la obra
* **\<columna 5>**: de tipo \<str\>, Pais de procedencia
* **\<columna 6>**: de tipo \<str\>, Estreno de la filmacion
* **\<columna 7>**: de tipo \<int\>, Año de filmacion
* **\<columna 8>**: de tipo \<str\>, Clasificacion
* **\<columna 9>**: de tipo \<str\>, Duracion
* **\<columna 10>**: de tipo \<str\>, Clasificacion del contenido
* **\<columna 11>**: de tipo \<str\>, Descripcion del contenido
....

## Tipos implementados

Peliculas=(Peliculas,(id,tipo,titulo,nombre,casting,pais,estreno,año de filmacion,puntuacion,duracion,clasificacion,descripcion))
Escribo el tipo de produccion y luego añado toda la informacion adicional

## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<funciones.py\>

* **<importaciones>**: importamos todo lo necesario para realizar el codigo
* **<leer_titulos()>**: definimos una funcion con el proposito de seleccionar y categorizar la informacion obtenida de los datos; para ello primero hacemos que acceda a la informacion y establecemos un lector con su sistema de lectura, añadimos el metodo que debe seguir para leer la informacion; establecemos una condicion, dependieno del tipo de filmacion hara un print u otro y por ultimo retornamos la clasificacion obtenida.
* **<cuenta_titulos()>**:funcion que te da la cantidad total de titulos
* **<obtener_titulos()>**:te da un listado de titulos 
* **<peliculas_de_mas_duracion()>**:esta funcion busca la mejor calificacion de cada pelicula y te devuelve el titulo de esta
* **<ordena_por_año()>**: Mediante el año de estreno te ordena los titulos
* **<agrupa_por_año()>**: Te agrupa por año cada titulo


### \<test.py\>

* **<test funcion 1>**: importamos lo que hemos hecho en funciones para comprobar si funciona
* **<test funcion 2>**: procedemos a especificar que lea los 20 primeros
* **<test funcion 3>**: hacemos un print de la funcion
* **<test funcion 4>**: hacemos un print de la funcion
* **<test funcion 5>**: hacemos un print de la funcion
* **<test funcion 6>**: hacemos un print de la funcion
* **<test funcion 7>**: hacemos un print de la funcion
