import os

from src.config.auth import AuthConfig


class Config:
    @classmethod
    def build(cls):
        app_name = os.getenv('TW_APP_NAME', 'twitter-client')
        result_file = os.getenv('TW_RESULT_FILE', '/tmp/twitter-api-results')
        auth = AuthConfig.build()
        return cls(app_name=app_name, result_file=result_file, auth=auth)

    def __init__(self, app_name, result_file, auth):
        self.app_name = app_name
        self.result_file = result_file
        self.auth = auth


