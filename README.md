# Big-Data-Analytics
In this repository I am showcasing sample big data analytics in hadoop using docker containerization.

1. I am using Macbook m1 with arm64 architechture, so I used this hadoop image :
```

docker pull bugbond/hadoop-spark-pig-hive-arm64

```
2. After the pulling is complete, execute this command for defining the ports and start the container:
```
docker run -it --name myhadoop -p 9000:9000 -p 2122:2122 -p 50070:50070 -p 50010:50010 -p 50075:50075 -p 50020:50020 -p 50090:50090 -p 8088:8088 -p 8030:8030 -p 8031:8031 -p 8032:8032 -p 8033:8033 -p 8040:8040 -p 8042:8042 -p 8080:8080 -p 8081:8081 -p 10000:10000 -p 9083:9083 suhothayan/hadoop-spark-pig-hive:2.9.2 bash

```
Note: To restart the container ( ``` docker exec -it myhadoop bash ```)
