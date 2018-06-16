import os


class AuthConfigurationError(Exception):
    pass


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
