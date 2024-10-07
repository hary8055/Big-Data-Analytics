# Big-Data-Analytics
In this repository I am showcasing sample big data analytics in hadoop using docker containerization.

## Setting up Hadoop

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
    Note : You can monitor the upload by accesing HDFS Web interface at (http://localhost:50070)

## MapReduce 

1. Inside a directory for scripts create mapper.py and reducer.py using ``` touch ```
2. Change the permissions of both files:
   ```

   chmod 777 mapper.py reducer.py

   ```
3. The mapper and reducer for this job is available in this repository
4. Submitting the mapreduce job to YARN:
   ```
   
   hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
     -input /home/datasrc/bigDataTask/trips.csv \
     -output /home/datasrc/output_avg_price_by_cabin_final \
     -mapper "python3 /home/datasrc/scripts/mapper.py" \
     -reducer "python3 /home/datasrc/scripts/reducer.py"
   
  ```

     **Note**: Specify the python version in your code.
     Monitor job specific details using YARN web interface at (http://localhost:8080)
5. To retrieve the results: ``` hadoop fs -cat /home/dataout/part-00000 ```



   
