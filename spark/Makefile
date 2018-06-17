SHELL	:= /bin/bash
RM 		:= rm -rf

SPARK_HOME 	?= $$HOME/lib/spark-2.3.0-bin-hadoop2.7
SPARK_BIN 	:= $(SPARK_HOME)/bin
SUBMIT 		:= $(SPARK_BIN)/spark-submit


NAME 			?= spark-examples
VERSION 		?= 1.0
SCALA_VERSION 	?= 2.11
JAR 			:= target/scala-$(SCALA_VERSION)/$(NAME)_$(SCALA_VERSION)-$(VERSION).jar

build:
	@cd examples; sbt package

run:
	cd examples; $(SUBMIT) --class "examples.sql.Application" --master local[*] $(JAR)

clean:
	@cd examples; $(RM) spark-warehouse/ project/ target/ | echo "Example project is clean"
