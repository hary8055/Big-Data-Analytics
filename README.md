# Big-Data-Analytics
In this repository I am showcasing sample big data analytics in hadoop using docker containerization.

1. I am using Macbook m1 with arm64 architechture, so I used this hadoop image :
```

docker pull bugbond/hadoop-spark-pig-hive-arm64

```
2. After the pulling is complete, execute this command for defining the ports and start the container:
```
docker run -it --name bigtools -p 9000:9000 -p 2122:2122 -p 50070:50070 -p 50010:50010 -p 50075:50075 -p 50020:50020 -p 50090:50090 -p 8088:8088 -p 8030:8030 -p 8031:8031 -p 8032:8032 -p 8033:8033 -p 8040:8040 -p 8042:8042 -p 8080:8080 -p 8081:8081 -p 10000:10000 -p 9083:9083 bugbond/hadoop-spark-pig-hive-arm64:latest bash

```
Note: To restart the container ( ``` docker exec -it bigtools bash ```)

3. Update Ubuntu: ``` apt update ```
4. Install Vim editor: ``` apt install vim ```
5. Set up Hadoop environment variables:
   ``` vim ~/.bashrc ```
   Add the following lines:
   ```

   export HADOOP_HOME=/usr/local/hadoop
   export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
   export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

   ```
6. Source the file : ``` source ~/.bashrc ```
7. Now the environment is set up, I am using a Flight PNR dataset from kaggle which is of 3,82 GB and the aim is to calculate average price of each cabin classes.
8. Created a directory inside home called 'datasrc'
9. Open another terminal in your machine and use this command to copy the dataset into docker:
    ```

    docker cp /Users/harikrishnans/Downloads/trips.csv 2833afcfec21:/home/datasrc

    ```
10. Creating directory in HDFS:
    ```
    hadoop fs -mkdir -p /home/datasrc/bigDataTask

    ```
11. Uploading dataset to Hdfs:
    ```
    hadoop fs -put Trips.csv /home/datasrc/bigDataTask

    ```
    Note : You can monitor the upload by accesing HDFS Web interface at ``` (http://localhost:50070) ```
   
