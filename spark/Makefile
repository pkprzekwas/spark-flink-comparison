SHELL	:= /bin/bash
RM 		:= rm -rf

SPARK_HOME 	?= $$HOME/lib/spark-2.3.0-bin-hadoop2.7
SPARK_BIN 	:= $(SPARK_HOME)/bin
SUBMIT 		:= $(SPARK_BIN)/spark-submit

NAME 			?= spark-examples
VERSION 		?= 1.0
SCALA_VERSION 	?= 2.11
JAR 			:= target/scala-$(SCALA_VERSION)/$(NAME)_$(SCALA_VERSION)-$(VERSION).jar

APP ?= sql

build:
	@sbt package

run:
	@$(SUBMIT) --class "examples.$(APP).Application" --master local[*] $(JAR)

clean:
	@$(RM) spark-warehouse/ project/ target/ | echo "Example project is clean"
