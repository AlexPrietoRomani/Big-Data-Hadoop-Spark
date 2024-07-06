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

![Creación de carpea](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/Paso%201.png "Creación de carpeta")

### Creamos el txt:

Para el caso de que los datos sean muy pocos y se pueda copiar los datos manualmente
```
nano casoDePrueba.txt
```
![Creación de data](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/Paso2-creardata.png "Creación de casoDePrueba.txt")

Para el caso de ser datos grandes
```
cp "Ruta especifica del archivo en Windows añadiendo /mnt" "Ruta en Ubuntu"
```
ejemplo:
```
cp /mnt/c/Temp/casoDePrueba.txt /home/hadoop/actividad1
```
Ingresamos la data: copiamos la dara de casoDePrueba.txt

Guardamos(Ctrl+S) y salimos(Ctrl+X)

![Ingrasamos de data](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/Paso2-data.png "Ingresamos data en casoDePrueba.txt")

## Paso 2:
### Caso con código python:
#### 1. Creamos el mapper:
```
nano mapper.py
```

Dentro del archivo copiamos el código de mapper.py

Guardamos(Ctrl+S) y salimos(Ctrl+X)

![Mapper](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/CrearMapper.png "Mapper.py")

#### Hacemos que sea ejecutable:
```
chmod +x mapper.py
```

#### 2. Creamos el combiner:
```
nano combiner.py
```

Dentro del archivo copiamos el código de combiner.py

Guardamos(Ctrl+S) y salimos(Ctrl+X)

![Combiner](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/CrearCombiner.png "Combiner.py")

#### Hacemos que sea ejecutable:
```
chmod +x combiner.py
```

#### 3. Creamos el reducer:
```
nano reducer.py
```

Dentro del archivo copiamos el código de reducer.py

Guardamos(Ctrl+S) y salimos(Ctrl+X)

![Reducer](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/CrearReducer.png "Reducer.py")

#### Hacemos que sea ejecutable:
```
chmod +x reducer.py
```
![Paso2final](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/Paso2final.png "Paso2final")

#### Probar localmente:

Ejecuta el siguiente comando para probar localmente:
```
cat casoDePrueba.txt | ./mapper.py | sort | ./combiner.py | sort | ./reducer.py
```

![Probar en Local](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/Probarejecuci%C3%B3n.png "Probarejecución")

## Paso 3:

### Preparar Hadoop para la ejecución

** Inicio de Hadoop:**
- Iniciar el clúster de Hadoop:
```
start-dfs.sh
```

- Inicie el administrador de nodos y el administrador de recursos:
```
start-yarn.sh
```

- Para comprobar si los servicios se ejecutan según lo previsto, utilice el siguiente comando:
```
jps
```

- Accede al nodo Namenode:
```
http://localhost:9870
```

- Acceda a Hadoop Resource Manager:
```
http://localhost:8088
```

![IniciarHadoop](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/IniciarHadoop.png "IniciarHadoop")

- Crea un directorio de entrada en HDFS:
```
hadoop fs -mkdir -p /home/hadoop/input/actividad1
```

- Copia el archivo de entrada a HDFS:
```
hadoop fs -put casoDePrueba.txt /home/hadoop/input/actividad1
```

- Para visualizar el archivo en la carpeta de hdfs:
```
hdfs dfs -ls /home/hadoop/input/actividad1
```

![Copiar data a HDFS](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/Copiar%20data%20a%20HDFS.png "Copiar data a HDFS")

- En caso equivocarte, puedes eliminar el archivo creado con:
```
hdfs dfs -rm /home/hadoop/input/actividad1/casoDePrueba.txt
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

![Paso3 EjecutarHadoop](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/Paso3%20EjecutarHadoop.png "Paso3 EjecutarHadoop")

## Paso 5:
### Verificar los resultados:

Ver los resultados:
```
hadoop fs -cat /home/hadoop/output/actividad1/part-00000 | head
```

![Paso3 ResultEjecutarHadoop](https://github.com/AlexPrietoRomani/Hadoop-MappReduce-Linux/blob/325a9697c861321b23faa64fb6e2e494580048c0/Actividad%201/imagenes/Paso3%20ResultEjecutarHadoop.png "Paso3 ResultEjecutarHadoop")

Si deseas eliminar la salida para futuras ejecuciones
```
hadoop fs -rm -r /home/hadoop/output/actividad1/
```
