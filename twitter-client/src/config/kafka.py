import os


class KafkaConfig:
    @classmethod
    def build(cls):
        host = os.getenv('TW_KAFKA_HOST')
        port = os.getenv('TW_KAFKA_PORT')
        topic = os.getenv('TW_KAFKA_TOPIC')
        return cls(topic=topic, kafka_host=host, kafka_port=port)

    def __init__(self, topic, kafka_host='localhost', kafka_port=9092):
        self.topic = topic
        self.host = kafka_host
        self.port = kafka_port
        self.url = f'{kafka_host}:{kafka_port}'
