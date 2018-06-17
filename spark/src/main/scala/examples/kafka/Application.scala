package examples.kafka

import org.apache.log4j.{Level, Logger}
import org.apache.spark.SparkConf
import org.apache.spark.streaming.{Seconds, StreamingContext}

import org.apache.kafka.clients.consumer.ConsumerRecord
import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.spark.streaming.kafka010._
import org.apache.spark.streaming.kafka010.LocationStrategies.PreferConsistent
import org.apache.spark.streaming.kafka010.ConsumerStrategies.Subscribe


object Application {

  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.ERROR)

    val appName = "TwitterReaderExample"
    val master = "local[2]"

    val conf = new SparkConf()
      .setAppName(appName)
      .setMaster(master)

    val ssc = new StreamingContext(conf, Seconds(2))

    process(ssc)

    ssc.start()
    ssc.awaitTermination()
  }

  def process(ssc: StreamingContext): Unit = {
    println("Processing Twitter stream...")

    val kafkaParams = Map[String, Object](
      "bootstrap.servers" -> "localhost:9092",
      "key.deserializer" -> classOf[StringDeserializer],
      "value.deserializer" -> classOf[StringDeserializer],
      "group.id" -> "use_a_separate_group_id_for_each_stream",
      "auto.offset.reset" -> "latest",
      "enable.auto.commit" -> (false: java.lang.Boolean)
    )

    val topics = Array("twitter_stream_topic")

    val stream = KafkaUtils.createDirectStream[String, String](
      ssc,
      PreferConsistent,
      Subscribe[String, String](topics, kafkaParams)
    )

    stream.foreachRDD { rdd =>
      println("RDD:")
      rdd.foreach(println)
    }
  }
}
