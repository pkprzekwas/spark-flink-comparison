package examples.streaming

import org.apache.spark._
import org.apache.spark.streaming._
import org.apache.log4j.{Level, Logger}


object Application {

  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.ERROR)

    val appName = "StreamingExample"
    val master = "local[2]"

    val conf = new SparkConf()
      .setAppName(appName)
      .setMaster(master)

    val ssc = new StreamingContext(conf, Seconds(5))

    val lines = ssc.socketTextStream("localhost", 9999)

    val words = lines.flatMap(_.split(" "))
    val pairs = words.map(word => (word, 1))
    val wordCounts = pairs.reduceByKey(_ + _)

    wordCounts.print()

    ssc.start()
    ssc.awaitTermination()
  }
}
