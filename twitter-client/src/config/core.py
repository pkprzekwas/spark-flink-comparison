import os

from src.config.auth import AuthConfig
from src.config.sink import SinkConfig


class Config:
    @classmethod
    def build(cls):
        app_name = os.getenv('TW_APP_NAME', 'twitter-client')
        auth = AuthConfig.build()
        sink = SinkConfig.build()
        return cls(app_name=app_name, auth=auth, sink=sink)

    def __init__(self, app_name, result_file, auth, sink):
        self.app_name = app_name
        self.auth = auth
        self.sink = sink

