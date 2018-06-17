
name := "spark-examples"

version := "1.0"

scalaVersion := "2.11.0"

val sparkVersion = "2.3.1"

libraryDependencies += "org.apache.spark" %% "spark-sql" % sparkVersion

libraryDependencies += "org.apache.spark" %% "spark-streaming_2.11" % sparkVersion

libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka-0-10_2.11" % sparkVersion
