import os
from enum import Enum

from src.config.kafka import KafkaConfig


class SinkType(Enum):
    CONSOLE = 'STDOUT'
    FILE = 'FILE'
    KAFKA = 'KAFKA'


class SinkConfig:
    @classmethod
    def build(cls):
        sink_type = os.getenv('TW_SINK_TYPE', SinkType.CONSOLE)

        if sink_type == SinkType.KAFKA:
            kafka = KafkaConfig.build()
            return cls(type=sink_type, kafka=kafka)

        elif sink_type == SinkType.FILE:
            file_path = os.getenv('TW_SINK_FILE')
            return cls(type=sink_type, file_path=file_path)

        return cls(type=sink_type)

    def __init__(self, type, kafka=None, file_path=None):
        self.type = type
        self.kafka = kafka
        self.file_path = file_path
