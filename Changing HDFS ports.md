To change the HDFS namenode UI start the container using the required ports:
```

 docker run -it --name bigtools -p 9000:9000 -p 2122:2122 -p 9870:9870 -p 50010:50010 -p 50075:50075 -p 50020:50020 -p 50090:50090 -p 8088:8088 -p 8030:8030 -p 8031:8031 -p 8032:8032 -p 8033:8033 -p 8040:8040 -p 8042:8042 -p 8080:8080 -p 8081:8081 -p 10000:10000 -p 9083:9083 bugbond/hadoop-spark-pig-hive-arm64:latest bash

```
