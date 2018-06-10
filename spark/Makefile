SPARK_HOME  ?= $$HOME/spark-2.3.0-bin-hadoop2.7
SPARK_BIN   := $(SPARK_HOME)/bin
SUBMIT	    := $(SPARK_BIN)/spark-submit

example-run:
	@echo "Running the example..."
	@cd simple; sbt package
	@cd simple; $(SUBMIT) --class "SimpleApp" --master local[*] target/scala-2.11/simple-project_2.11-1.0.jar

