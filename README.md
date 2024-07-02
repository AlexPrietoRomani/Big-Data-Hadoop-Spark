# Hadoop-MappReduce-Linux
Actividad Realizada para realizar ejecución de 3 problemas con la aplicación de Hadoop MappReduce.

# Guías para cada actividad

## Preliminar

### Uso de WSL en Windows ( En caso uses Windows):

```
Leer el archivo WSL.md
```

### Instalación de HDF y Hadoop en Ubuntu.

```
Leer el archivo Instalacion-Hadoop.md
```

## Actividades realizadas:

### Actividad 1:
- Planteamiento del problema:
Dado un dataset que contenga entradas con la forma “persona;tienda;gasto”, crea un programa llamado mediaGastadoPersonaTienda que para cada persona indique su gasto medio por tienda, siguiendo el formato persona;tienda;gastomedio.

- Dataset: casoDePrueba.txt
  
- Cabecera del dataset:

Alice;Tienda1;50   
Alice;Tienda2;20    
Bob;Tienda1;30    
Alice;Tienda1;100    
Bob;Tienda1;20    

- Salida esperada:

Alice;Tienda1;75    
Alice;Tienda2;20    
Bob;Tienda1;25    

```
Leer el archivo Actividad-1.md
```

### Actividad 2: 
- Planteamiento del problema:

Deben implementar un programa MapReduce escrito en Java o Python (a elegir) que, para cada patente de cite75_99.txt, obtenga la lista de las que la citan:
  • Posible implementación:
    ◦ El mapper obtiene cada línea del fichero de entrada, separar los campos y los invierte (para obtener como clave intermedia la patente citada y como valor intermedio la patente que la cita), por ejemplo:
        3858245, 3755824 → 3755824 3858245 
    ◦ El reducer, para cada patente recibe como valor una lista de las que la citan, ordena esa lista numéricamente y la convierte en un string de números separados por coma
        3755824 {3858245 3858247. . . } → 3755824 3858245, 3858247...
  • Formato de salida: patente patente1,patente2... (la separación entre la clave y los valores debe ser un tabulado)
    ◦ La salida debe de estar ordenada por la clave (patentes citadas) y los valores también deben estar ordenados por patentes citantes.
    ◦ Los valores se deben guardar separados por coma, sin espacios en blanco entre ellos.
    ◦ Deben tener en cuenta la cabecera, para que no aparezca en la salida (el fichero de entrada no debe modificarse de ninguna manera)

- Dataset:

Para este ejercicio utilizarán el fichero de entrada cite75_99.txt que puede ser descargado del National Bureau of Economic Research (NBER) de EEUU (http://www.nber.org/patents/).
Una descripción detallada de este fichero puede encontrarse en:
Hall, B. H., A. B. Jaffe, and M. Trajtenberg (2001). "The NBER Patent Citation Data File: Lessons, Insights and Methodological Tools." NBER Working Paper 8498.
Este fichero contiene citas de patentes emitidas entre 1975 y 1990 en los EEUU. Es un fichero CSV (comma-separated values) con más de 16,5 millones de filas.
La primera línea contiene una cabecera con la descripción de las columnas. Cada una de las otras líneas indica una cita que la patente con el número de la primera columna ha hecho a la patente con el número en la segunda. Por ejemplo, la segunda fila indica que la patente nº 3858241 ("citing" o citante) hace una cita a la patente nº 956203 ("cited" o citada).
El fichero está ordenado por las patentes citantes. Así podemos ver que la patente nº 3858241 cita a otras 5 patentes.

- Cabecera del dataset:

"CITING","CITED" 
 3858241,956203 
 3858241,1324234 
 3858241,3398406 
 3858241,3557384 
 3858241,3634889 
 3858242,1515701 
 3858242,3319261 
 3858242,3668705

```
Leer el archivo Actividad-2.md
```

### Actividad 3: 
- Planteamiento del problema:
```
Leer el archivo Actividad-3.md
```
