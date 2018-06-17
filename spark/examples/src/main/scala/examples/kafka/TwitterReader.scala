package examples.kafka

import org.apache.log4j.{Level, Logger}
import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}

object TwitterReader {

  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.ERROR)

    val appName = "TwitterReaderExample"
    val master = "local[2]"

    val conf = new SparkConf()
      .setAppName(appName)
      .setMaster(master)

    val ssc = new StreamingContext(conf, Seconds(5))

    process(ssc)

    ssc.start()
    ssc.awaitTermination()
  }

  def process(ssc: StreamingContext): Unit = {
    println("Processing Twitter stream...")
  }
}
