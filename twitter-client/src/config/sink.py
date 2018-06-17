import os
from enum import Enum

from src.config.kafka import KafkaConfig


class SinkType(Enum):
    FILE = 'FILE'
    KAFKA = 'KAFKA'
    CONSOLE = 'STDOUT'


class SinkConfig:
    @classmethod
    def build(cls):
        sink_type = os.getenv('TW_SINK_TYPE', SinkType.CONSOLE)

        if sink_type == SinkType.KAFKA.value:
            kafka = KafkaConfig.build()
            return cls(sink_type=sink_type, kafka=kafka)

        elif sink_type == SinkType.FILE.value:
            file_path = os.getenv('TW_SINK_FILE')
            return cls(sink_type=sink_type, file_path=file_path)

        return cls(sink_type=sink_type)

    def __init__(self, sink_type, kafka=None, file_path=None):
        self.type = sink_type
        self.kafka = kafka
        self.file_path = file_path
