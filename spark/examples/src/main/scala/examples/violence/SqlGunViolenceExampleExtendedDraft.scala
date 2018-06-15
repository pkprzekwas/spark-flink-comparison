package examples.violence

import org.apache.log4j.{Level, Logger}
import org.apache.spark.sql.{DataFrame, Dataset, SparkSession}


object SqlGunViolenceExampleExtendedDraft {

  // More on the dataset: https://www.kaggle.com/jameslko/gun-violence-data
  private final val GunViolenceDataset = "/home/pprzekwa/datasets/gun-violence-data_01-2013_03-2018.csv"

  case class GunViolence(incident_id: String, date: String, state: String, city_or_county: String,
                         address: String, n_killed: String, incident_url: String, source_url: String,
                         incident_url_fields_missing: String, congressional_district: String, gun_stolen: String,
                         gun_type: String, incident_characteristics: String, latitude: String,
                         location_description: String, longitude: String, n_guns_involved: String, notes: String,
                         participant_age: String, participant_age_group: String, participant_gender: String,
                         participant_name: String, participant_relationship: String, participant_status: String,
                         participant_type: String, sources: String, state_house_district: String,
                         state_senate_district: String)

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

  private def readUsingCaseClass(spark: SparkSession): Dataset[GunViolence]  = {
    import spark.implicits._
    spark
      .read
      .option("header", value = true)
      .csv(GunViolenceDataset)
      .as[GunViolence]
  }

}
