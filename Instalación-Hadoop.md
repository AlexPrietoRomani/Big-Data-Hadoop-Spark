# Instalación Hadoop

## Paso 1: Requisitos previos
- Asegúrese de que su sistema esté actualizado y que Java sea imprescindible, así que comencemos ejecutando los siguientes comandos:
```
sudo apt update
sudo apt upgrade -y
sudo apt install openjdk-8-jre-headless
```
Para verificar la instalación, compruebe la versión de Java en su sistema:
```
java -version
```
En caso tengas 2 versiones de java, y seleccionar el que quieras usar:
```
sudo update-alternatives --config java
```

## Paso 2: Crear un usuario para Hadoop, instalar y configurar SSH
- Creación de un usuario para Hadoop
```
sudo adduser hadoop
```
- Para otorgar privilegios de superusuario al nuevo usuario, inclúyalo en el grupo sudo:
```
sudo usermod -aG sudo hadoop
```
- Al finalizar, cambie al usuario 'hadoop'
```
sudo su - hadoop
```
- Instale el servidor y el cliente OpenSSH:
```
sudo apt install ssh
```
- Utilice el siguiente comando para generar claves privadas y públicas:
```
ssh-keygen -t rsa
```
Durante este paso, se le solicitarán las siguientes consultas:

Especifique el destino para guardar la clave (pulse Intro para guardarla en el directorio de inicio).
Cree una frase de contraseña para las claves (opte por dejarla en blanco para que no haya frase de contraseña).

- Agregue la clave pública a authorized_keys:
```
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
- Usando el comando chmod, cambie los permisos de archivo de authorized_keys:
```
sudo chmod 640 ~/.ssh/authorized_keys
```
- Iniciar el servicio SSH
```
sudo service ssh start
```
- Confirme la configuración de SSH:
```
ssh localhost
```
## Paso 3: Descarga e instala Apache Hadoop
- Visite la página oficial de descarga de Apache Hadoop para buscar la versión reciente y descárguela utilizando el comando que se indica a continuación:
https://downloads.apache.org/hadoop/common/stable/?ref=learnubuntu.com
```
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz
```
- Extraer el archivo
```
tar -xvzf hadoop-3.4.0.tar.gz
```
- Mueva el archivo extraído a /usr/local/hadoop usando el siguiente comando:
```
sudo mv hadoop-3.4.0 hadoop
```
- Cree un directorio mediante el comando mkdir para almacenar registros:
```
sudo mkdir /home/hadoop/hadoop/logs
```
- Modifique la propiedad del directorio /usr/local/hadoop al usuario hadoop:
```
sudo chown -R hadoop:hadoop /home/hadoop/hadoop
```
- Para la configuración de la variable de entorno de Hadoop, abra el archivo .bashrc mediante el siguiente comando:
```
sudo nano ~/.bashrc
```
- Navegue hasta el final del archivo presionando ctrl + / y luego ctrl + v y luego inserte las siguientes líneas:
Nota: La ruta de JAVA_HOME debe ser en donde se encuentre instalado tu java y la versión de la misma
Para poder saber que ruta tiene tu versión de java:
```
update-java-alternatives -l
```
Y luego procedemos a realizar el cambio:
```
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
export HADOOP_HOME=/home/hadoop/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
```
Guarde los cambios pulsando Ctrl+S y salga del editor de nanotexto pulsando C, trl+x

- Para habilitar los cambios, obtenga el archivo .bashrc
```
source ~/.bashrc
```
## Paso 4: Configurar las variables de entorno de Java
Las funciones principales de Hadoop, es decir, YARN, HDFS, MapReduce y la configuración del proyecto relacionada con Hadoop, deben estar habilitadas para poder utilizarlo.

Defina las variables de entorno java en hadoop-env.sh archivo para que:

- Abra el archivo hadoop-env.sh
```
sudo nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```
- Busque el "JAVA_HOME de exportación" y configúrelo agregando la línea:
```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
Guarde los cambios y salga del editor

- Comprobar la versión de Hadoop
```
hadoop version
```
## Paso 5: Configurar Hadoop

- Abra el archivo core-site.xml con el siguiente comando:
```
sudo nano $HADOOP_HOME/etc/hadoop/core-site.xml
```
- Agregue las siguientes líneas entre <Configuration> </Configuration>
```
<property>

      <name>fs.default.name</name>

      <value>hdfs://localhost:9000</value>

      <description>The default file system URI</description>

   </property>
```
Guarde los cambios y salga del editor

- Cree un directorio para almacenar metadatos de nodo mediante el siguiente comando:
```
sudo mkdir -p /home/hadoop/hdfs/{namenode,datanode}
```
- Otorgue la propiedad del directorio creado al usuario de Hadoop:
```
sudo chown -R hadoop:hadoop /home/hadoop/hdfs
```
- Abra el archivo hdfs-site.xml con el siguiente comando:
```
sudo nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```
- Y agregue las siguientes líneas entre <Configuración> </Configuración>
```
<property>

      <name>dfs.replication</name>

      <value>1</value>

   </property>


   <property>

      <name>dfs.name.dir</name>

      <value>file:///home/hadoop/hdfs/namenode</value>

   </property>


   <property>

      <name>dfs.data.dir</name>

      <value>file:///home/hadoop/hdfs/datanode</value>

</property>
```
Guarde los cambios y salga del editor

- Abra el archivo mapred-site.xml con el siguiente comando:
```
sudo nano $HADOOP_HOME/etc/hadoop/mapred-site.xml
```
- Y agregue las siguientes líneas entre <Configuración> </Configuración>
```
<property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
</property>
<property>
  <name>yarn.app.mapreduce.am.env</name>
  <value>HADOOP_MAPRED_HOME=/home/hadoop/hadoop</value>
</property>
<property>
  <name>mapreduce.map.env</name>
  <value>HADOOP_MAPRED_HOME=/home/hadoop/hadoop</value>
</property>
<property>
  <name>mapreduce.reduce.env</name>
  <value>HADOOP_MAPRED_HOME=/home/hadoop/hadoop</value>
</property>
```
Guarde los cambios y salga del editor

- Abra el archivo yarn-site.xml con el siguiente comando:
```
sudo nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
```
- Y agregue las siguientes líneas entre <Configuración> </Configuración>
```
<property>

      <name>yarn.nodemanager.aux-services</name>

      <value>mapreduce_shuffle</value>

</property>
```
Guarde los cambios y salga del editor

- Para validar la configuración de Hadoop y formatear el NameNode de HDFS, utilice el siguiente comando:
```
hdfs namenode -format
```
## Paso 6: Iniciar el clúster de Hadoop
- Iniciar el clúster de Hadoop
```
start-dfs.sh
```
- A continuación, inicie el administrador de nodos y el administrador de recursos:
```
start-yarn.sh
```
- Para comprobar si los servicios se ejecutan según lo previsto, utilice el siguiente comando:
```
jps
```
## Paso 7: Accede al nodo Namenode:

```
http://localhost:9870
```

## Paso 8: Acceda a Hadoop Resource Manager:

```
http://localhost:8088
```

