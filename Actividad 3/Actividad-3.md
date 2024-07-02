# Actividad 3

## Cambiamos a usuario hadoop
```
sudo su - hadoop
```
En caso creaste un usuario especifico para realizar las actividades.

## Paso 1:

### Creamos una carpeta para guardar los archivos
```
mkdir personasQueCompranEnMuchasTiendas
```

Nota: 
```
ls
```
Podemos observar la carpeta creada

### Ingresamos a la carpeta
```
cd personasQueCompranEnMuchasTiendas
```

### Creamos el txt:

Importamos el archivo de un directorio de Windows
```
cp "Ruta especifica del archivo en Windows añadiendo /mnt" "Ruta en Ubuntu"
```
ejemplo:
```
cp /mnt/c/Temp/casoDePrueba.txt /home/hadoop/personasQueCompranEnMuchasTiendas
```
Ingresamos la data: copiamos la dara de casoDePrueba.txt

Guardamos(Ctrl+S) y salimos(Ctrl+X)

## Paso 2:
### Caso con código python:
#### 1. Creamos el mapper:
```
nano mapperPersonasQueCompranEnMuchasTiendas.py
```
---------
Nota:
Dentro de la carpeta personasQueCompranEnMuchasTiendas de la Actividad 3, tendremos el archivo "mapperPersonasQueCompranEnMuchasTiendas.py" el cual posee errores, tienes que identificar y corregir los errores.
---------
Solución:
Dentro de la carpeta Solución de la Actividad 3, se encuentra "mapperPersonasQueCompranEnMuchasTiendas.py" que es el archivo corregido, el cual podemos usar de referencia para copiarlo.
---------
Guardamos(Ctrl+S) y salimos(Ctrl+X)

#### Hacemos que sea ejecutable:
```
chmod +x mapperPersonasQueCompranEnMuchasTiendas.py
```

#### 2. Creamos el combiner:
```
nano combinerPersonasQueCompranEnMuchasTiendas.py
```
---------
Nota:
Dentro de la carpeta personasQueCompranEnMuchasTiendas de la Actividad 3, tendremos el archivo "combinerPersonasQueCompranEnMuchasTiendas.py" el cual posee errores, tienes que identificar y corregir los errores.
---------
Solución:
Dentro de la carpeta Solución de la Actividad 3, se encuentra "combinerPersonasQueCompranEnMuchasTiendas.py" que es el archivo corregido, el cual podemos usar de referencia para copiarlo.
---------

Guardamos(Ctrl+S) y salimos(Ctrl+X)

#### Hacemos que sea ejecutable:
```
chmod +x combinerPersonasQueCompranEnMuchasTiendas.py
```

#### 3. Creamos el reducer:
```
nano reducerPersonasQueCompranEnMuchasTiendas.py
```
---------
Nota:
Dentro de la carpeta personasQueCompranEnMuchasTiendas de la Actividad 3, tendremos el archivo "reducerPersonasQueCompranEnMuchasTiendas.py" el cual posee errores, tienes que identificar y corregir los errores.
---------
Solución:
Dentro de la carpeta Solución de la Actividad 3, se encuentra "reducerPersonasQueCompranEnMuchasTiendas.py" que es el archivo corregido, el cual podemos usar de referencia para copiarlo.
---------

Guardamos(Ctrl+S) y salimos(Ctrl+X)

#### Hacemos que sea ejecutable:
```
chmod +x reducerPersonasQueCompranEnMuchasTiendas.py
```

#### Probar localmente:

Ejecuta el siguiente comando para probar localmente:
```
cat casoDePrueba.txt | ./mapperPersonasQueCompranEnMuchasTiendas.py | sort | ./combinerPersonasQueCompranEnMuchasTiendas.py | sort | ./reducerPersonasQueCompranEnMuchasTiendas.py
```

## Paso 3:

### Preparar Hadoop para la ejecución

Crea un directorio de entrada en HDFS:
```
hadoop fs -mkdir -p /user/hadoop/input/
```

Copia el archivo de entrada a HDFS:
```
hadoop fs -put casoDePrueba.txt /user/hadoop/input/
```

Para visualizar el archivo en la carpeta de hdfs:
```
hdfs dfs -ls /user/hadoop/input/
```

## Paso 4:

### Ejecutar el trabajo Hadoop:

Ejecuta el siguiente comando para iniciar el trabajo:
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
-mapper ./mapperPersonasQueCompranEnMuchasTiendas.py \
-file ./mapperPersonasQueCompranEnMuchasTiendas.py \
-combiner ./combinerPersonasQueCompranEnMuchasTiendas.py \
-file ./combinerPersonasQueCompranEnMuchasTiendas.py \
-reducer ./reducerPersonasQueCompranEnMuchasTiendas.py \
-file ./reducerPersonasQueCompranEnMuchasTiendas.py \
-input /user/hadoop/input/casoDePrueba.txt \
-output /user/hadoop/output/misalida
```

## Paso 5:
### Verificar los resultados:

Ver los resultados:
```
hadoop fs -cat /user/hadoop/output/misalida/part-00000 | head
```
Si deseas eliminar la salida para futuras ejecuciones
```
hadoop fs -rm -r /user/hadoop/output/misalida
```
