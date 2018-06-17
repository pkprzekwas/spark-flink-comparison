import os


class KafkaConfig:
    @classmethod
    def build(cls):
        config = dict(
            host=os.getenv('TW_KAFKA_HOST'),
            port=os.getenv('TW_KAFKA_PORT'),
            topic=os.getenv('TW_KAFKA_TOPIC')
        )

        if not all(config.values()):
            raise KafkaConfigurationError('Please provide configuration for Kafka.')

        return cls(**config)

    def __init__(self, topic, host='localhost', port=9092):
        self.topic = topic
        self.host = host
        self.port = port
        self.url = f'{host}:{port}'


class KafkaConfigurationError(Exception):
    pass
