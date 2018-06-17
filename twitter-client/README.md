# Twitter Client

The main purpose of this application is to connect to the Twitter API using `tweepy` client and send tweets to the
dedicated sink. Available sinks are: Apache Kafka, file and console.

### Quick Start (Kafka Sink)

1. [Setup local Apache Kafka.](../kafka/README.md)
2. Create virtualenv and install requirements:
```bash
make deps-install
``` 
3. Decrypt file with a configuration of environmental variables (optional). 
```bash
make vault-decrypt
```
You can also provide your own configuration and put to a `secrets` file. 
Example:
```bash
export TW_APP_NAME=Twitter-API-Client
export TW_CONSUMER_KEY=...
export TW_CONSUMER_SECRET=...
export TW_ACCESS_TOKEN=...
export TW_ACCESS_TOKEN_SECRET=...
export TW_SINK_TYPE=KAFKA
export TW_KAFKA_HOST=localhost
export TW_KAFKA_PORT=9092
export TW_KAFKA_TOPIC=twitter_stream
export TW_SINK_FILE=/tmp/twitter-api-results
```
4. Start the application
```bash
make app-start
```
5. To test if everything works correctly run Kafka consumer. 
```bash
make app-kafka-debug
```

### Tips and tricks

Pycharm envs configuration example:
```
TW_KAFKA_HOST=localhost
PYTHONUNBUFFERED=1
TW_SINK_TYPE=KAFKA
TW_KAFKA_PORT=9092
TW_KAFKA_HOST=localhost
TW_KAFKA_TOPIC=twitter_stream
TW_SINK_FILE=/tmp/twitter-api-results
TW_CONSUMER_KEY=<twitter_consumer_key>
TW_CONSUMER_SECRET=<twitter_consumer_secret>
TW_ACCESS_TOKEN=<twitter_access_token>
TW_ACCESS_TOKEN_SECRET=<twitter_access_token_secret>
```
