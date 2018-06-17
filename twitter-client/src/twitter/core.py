import tweepy


class TwitterApi(tweepy.API):
    @classmethod
    def build(cls, auth_config):
        auth = TwitterApi._login(auth_config)
        api = tweepy.API(auth)
        return api

    @staticmethod
    def _login(auth_config):
        auth = tweepy.OAuthHandler(auth_config.consumer_key, auth_config.consumer_secret)
        auth.set_access_token(auth_config.access_token, auth_config.access_token_secret)
        return auth


class TwitterStream:
    @classmethod
    def build(cls, api, filters=None, sink=None):
        stream = tweepy.Stream(
            auth=api.auth,
            listener=TwitterStreamListener(sink)
        )
        return cls(stream=stream, filters=filters)

    def __init__(self, stream, filters):
        self.stream = stream
        self.filters = filters

    def run(self):
        self.stream.filter(track=self.filters, async=True)


class TwitterStreamListener(tweepy.StreamListener):
    def __init__(self, sink=None):
        super().__init__()
        self._sink = sink

    def on_status(self, status):
        self._sink.send()

    def on_error(self, status_code):
        if status_code == 420:
            return False
