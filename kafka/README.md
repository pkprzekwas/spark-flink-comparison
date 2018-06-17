# Running Kafka locally

##### Prerequisites:
- Docker
- Docker-compose
- Apache Kafka (version - 1.1.0)

##### Quick start
1. Start Zookeeper instances in using Docker:
```bash
make zookeeper-start
```
2. Export `KAFKA_HOME` with a proper system path:
```bash
# example
export KAFKA_HOME=~/lib/kafka_2.11-1.1.0
```
3. Run Kafka server:
```bash
make kafka-start
```
At this point you should be able to connect to your Kafka instance on `http://localhost:9092`.

##### Cleaning up
1. Stop your Kafka server using `^C`.
2. Kill Zookeeper containers:
```bash
make zookeeper-stop
```
