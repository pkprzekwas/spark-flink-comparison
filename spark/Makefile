SPARK_HOME  ?= $$HOME/spark-2.3.0-bin-hadoop2.7
SPARK_BIN   := $(SPARK_HOME)/bin
SUBMIT	    := $(SPARK_BIN)/spark-submit

RM	    := rm -rf


example-build:
	@cd simple; sbt package

example-run: example-build
	@cd simple; $(SUBMIT) --class "SimpleApp" --master local[*] target/scala-2.11/simple-project_2.11-1.0.jar

example-clean:
	@cd simple; $(RM) spark-warehouse/ project/ target/ | echo "Example project is clean"
