from kafka import KafkaProducer

from src.config.core import Config
from src.twitter.sinks import KafkaSink
from src.twitter.core import TwitterApi, TwitterStream
from src.twitter.filters import world_cup_filters as wcf


def main():
    config = Config.build()

    api = TwitterApi.build(auth_config=config.auth)
    kafka_producer = KafkaProducer(bootstrap_servers=config.sink.kafka.url)
    kafka_sink = KafkaSink(topic=config.sink.kafka.topic, producer=kafka_producer)
    stream = TwitterStream.build(api=api, filters=wcf, sink=kafka_sink)
    stream.run()


if __name__ == '__main__':
    main()
