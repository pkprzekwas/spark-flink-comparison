package examples.sql

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql.{DataFrame, SparkSession}


object SqlGunViolenceExample {

  // More on the dataset: https://www.kaggle.com/jameslko/gun-violence-data
  private final val GunViolenceDataset = "/home/pprzekwa/datasets/gun-violence-data_01-2013_03-2018.csv"

  def main(args: Array[String]): Unit = {
    Logger.getLogger("org").setLevel(Level.ERROR)

    val spark = SparkSession
      .builder()
      .appName("Spark SQL basic example")
      .master("local")
      .getOrCreate()

    val crimes = readDatafile(spark)

    val crimesForCalifornia = getCityCrimesByRecordCount(spark, crimes, state="California")

    crimesForCalifornia.show(10)
  }

  private def getCityCrimesByRecordCount(spark: SparkSession, crimes: DataFrame, state: String): DataFrame = {
    import spark.implicits._
    crimes
      .filter($"state".rlike(state))
      .groupBy("city_or_county")
      .count()
      .orderBy($"count".desc)
  }

  private def readDatafile(spark: SparkSession): DataFrame = {
    spark
      .read
      .option("header", value = true)
      .csv(GunViolenceDataset)
  }

}
