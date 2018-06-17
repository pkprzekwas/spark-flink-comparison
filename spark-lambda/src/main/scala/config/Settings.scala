package config

import com.typesafe.config.ConfigFactory


object Settings {
  private val config = ConfigFactory.load()

  object WebLogGen {
    private val weblogGen = config.getConfig("clickstream")

    lazy val records: Int = weblogGen.getInt("records")
    lazy val timeMultiplier: Int = weblogGen.getInt("time_multiplier")
    lazy val pages: Int = weblogGen.getInt("pages")
    lazy val visitors: Int = weblogGen.getInt("visitors")
    lazy val filePath: String = weblogGen.getString("file_path")
  }
}
