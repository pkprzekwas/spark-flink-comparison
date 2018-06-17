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

        return cls(**credentials)

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret


class AuthConfigurationError(Exception):
    pass
