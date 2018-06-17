SHELL 	:= /bin/bash
DC 		:= docker-compose

KAFKA_HOME 	?= ~/lib/kafka_2.11-1.1.0
KAFKA_BIN 	:= $(KAFKA_HOME)/bin

ZOOKEEPER_COMPOSE := zookeeper/stack.yaml


zookeeper-start:
	@$(DC) -f $(ZOOKEEPER_COMPOSE) up -d

zookeeper-stop:
	@$(DC) -f $(ZOOKEEPER_COMPOSE) down

kafka-start:
	@$(KAFKA_BIN)/kafka-server-start.sh server.properties
