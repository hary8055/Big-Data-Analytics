1. To change the HDFS namenode UI start the container using the required ports:
```

 docker run -it --name bigtools -p 9000:9000 -p 2122:2122 -p 9870:9870 -p 50010:50010 -p 50075:50075 -p 50020:50020 -p 50090:50090 -p 8088:8088 -p 8030:8030 -p 8031:8031 -p 8032:8032 -p 8033:8033 -p 8040:8040 -p 8042:8042 -p 8080:8080 -p 8081:8081 -p 10000:10000 -p 9083:9083 bugbond/hadoop-spark-pig-hive-arm64:latest bash

```
Here I am changing namdnode UI port from previously 50070 to 9870

2. In the Hadoop environment locate the hadoop configuration directory which is usually ``` /usr/local/hadoop/etc/hadoop/ ```
3. Edit the ``` hdfs-site.xml ``` and add the following inside the configuration block:
   ```

   <property>
    <name>dfs.namenode.http-address</name>
    <value>0.0.0.0:9870</value>
   </property>

   ```
4. Also update the ``` core-site.xml ``` file:
   ```

   <configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
   </configuration>

   ```
5. Finaly update the ``` yarn-site.xml ``` file:
   ```

   <configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
   </configuration>

   ```
6. Format the HDFS namenode : ``` hdfs namenode -format ```
7. Start HDFS : ``` start-dfs.sh ``` , start YARN : ``` start-yarn.sh ```

   Check the web interface of HDFS at (http://localhost:9870)


