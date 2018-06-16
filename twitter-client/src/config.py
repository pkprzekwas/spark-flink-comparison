import os


class ConfigurationError(Exception):
    pass


class Config:

    @classmethod
    def build(cls):
        app_name = os.getenv('TW_APP_NAME', 'twitter-client')

        credentials = dict(
            consumer_key=os.getenv('TW_CONSUMER_KEY', None),
            consumer_secret=os.getenv('TW_CONSUMER_SECRET', None),
            access_token=os.getenv('TW_ACCESS_TOKEN', None),
            access_token_secret=os.getenv('TW_ACCESS_TOKEN_SECRET', None)
        )

        if not all(credentials.values()):
            raise ConfigurationError('Please provide credentials for Tweeter API.')

        return cls(app_name=app_name, credentials=credentials)

    def __init__(self, app_name, credentials):
        self.app_name = app_name,
        self.consumer_key = credentials['consumer_key']
        self.consumer_secret = credentials['consumer_secret']
        self.access_token = credentials['access_token']
        self.access_token_secret = credentials['access_token_secret']
