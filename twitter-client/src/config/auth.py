import os


class AuthConfig:
    @classmethod
    def build(cls):
        credentials = dict(
            consumer_key=os.environ.get('TW_CONSUMER_KEY', None),
            consumer_secret=os.environ.get('TW_CONSUMER_SECRET', None),
            access_token=os.environ.get('TW_ACCESS_TOKEN', None),
            access_token_secret=os.environ.get('TW_ACCESS_TOKEN_SECRET', None)
        )

        if not all(credentials.values()):
            raise AuthConfigurationError('Please provide credentials for Tweeter API.')

        return cls(credentials=credentials)

    def __init__(self, credentials):
        self.consumer_key = credentials['consumer_key']
        self.consumer_secret = credentials['consumer_secret']
        self.access_token = credentials['access_token']
        self.access_token_secret = credentials['access_token_secret']


class AuthConfigurationError(Exception):
    pass
