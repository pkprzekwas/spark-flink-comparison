import org.apache.spark.sql.SparkSession

object SimpleApp {

  def main(args: Array[String]) {

    val logFile = "/etc/hosts"

    val spark = SparkSession
      .builder
      .master("local")
      .appName("Simple Application")
      .getOrCreate()

    val logData = spark
      .read
      .textFile(logFile)
      .cache()

    val numAs = logData
      .filter(line => line.contains("a"))
      .count()

    val numBs = logData
      .filter(line => line.contains("b"))
      .count()

    println(s"Lines with a: $numAs, Lines with b: $numBs")

    spark.stop()
  }
}
