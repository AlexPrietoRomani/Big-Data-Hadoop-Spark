# Actividad 1

## Cambiamos a usuario hadoop
```
sudo su - hadoop
```
En caso creaste un usuario especifico para realizar las actividades.

## Paso 1:

### Creamos una carpeta para guardar los archivos
```
mkdir actividad1
```

Nota: 
```
ls
```
Podemos observar la carpeta creada

### Ingresamos a la carpeta
```
cd actividad1
```

### Creamos el txt:
```
nano casoDePrueba.txt
```

Ingresamos la data: copiamos la dara de casoDePrueba.txt

Guardamos(Ctrl+S) y salimos(Ctrl+X)

## Paso 2:
### Caso con código python:
#### Creamos el mapper:
```
nano mapper.py
```

Dentro del archivo copiamos el código de mapper.py

Guardamos(Ctrl+S) y salimos(Ctrl+X)

#### Hacemos que sea ejecutable:
```
chmod +x mapper.py
```

#### Creamos el combiner:
```
nano combiner.py
```

Dentro del archivo copiamos el código de combiner.py

Guardamos(Ctrl+S) y salimos(Ctrl+X)

#### Hacemos que sea ejecutable:
```
chmod +x combiner.py
```

#### Creamos el reducer:
```
nano reducer.py
```

Dentro del archivo copiamos el código de reducer.py

Guardamos(Ctrl+S) y salimos(Ctrl+X)

#### Hacemos que sea ejecutable:
```
chmod +x reducer.py
```

#### Probar localmente:

Ejecuta el siguiente comando para probar localmente:
```
cat casoDePrueba.txt | ./mapper.py | sort | ./combiner.py | sort | ./reducer.py
```

## Paso 3:

### Preparar Hadoop para la ejecución

Crea un directorio de entrada en HDFS:
```
hadoop fs -mkdir -p /home/hadoop/input/actividad1
```

Copia el archivo de entrada a HDFS:
```
hadoop fs -put casoDePrueba.txt /home/hadoop/input/actividad1
```

Para visualizar el archivo en la carpeta de hdfs:
```
hdfs dfs -ls /home/hadoop/input/actividad1
```

## Paso 4:

### Ejecutar el trabajo Hadoop:

Ejecuta el siguiente comando para iniciar el trabajo:
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
-files /home/hadoop/actividad1/mapper.py,/home/hadoop/actividad1/reducer.py \
-mapper /home/hadoop/actividad1/mapper.py \
-combiner /home/hadoop/actividad1/combiner.py \
-reducer /home/hadoop/actividad1/reducer.py \
-input /home/hadoop/input/actividad1/casoDePrueba.txt \
-output /home/hadoop/output/actividad1
```

## Paso 5:
### Verificar los resultados:

Ver los resultados:
```
hadoop fs -cat /home/hadoop/output/actividad1/part-00000
```
Si deseas eliminar la salida para futuras ejecuciones
```
hadoop fs -rm -r /home/hadoop/output/actividad1/part-00000
```
