
name := "spark-examples"

version := "1.0"

scalaVersion := "2.11.0"

val sparkVersion = "2.3.0"

libraryDependencies += "org.apache.spark" %% "spark-sql" % sparkVersion

libraryDependencies += "org.apache.spark" % "spark-streaming_2.11" % sparkVersion
