from src.config import Config
from src.twitter import TwitterApi, TwitterStream
from src.filters import programming_filters


def main():
    config = Config.build()
    api = TwitterApi.build(auth_config=config.auth)
    stream = TwitterStream.build(
        api=api,
        filters=programming_filters,
        result_file=config.result_file
    )
    stream.run()


if __name__ == '__main__':
    main()
