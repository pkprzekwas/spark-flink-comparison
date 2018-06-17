from src.config.logger import logger


class BaseSink:
    def send(self, data):
        logger.info(data)


class FileSink(BaseSink):
    def __init__(self, file_path):
        self._file = file_path

    def send(self, data):
        with open(self._file, "a") as f:
            f.write(str(data))


class KafkaSink(BaseSink):
    def __init__(self, producer, topic):
        self._topic = topic
        self._producer = producer

    def send(self, data):
        self._producer.send(self._topic, data)
