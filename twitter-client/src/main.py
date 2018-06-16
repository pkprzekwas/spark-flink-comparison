import tweepy

from src.config import Config
from src.logger import logger


def main():
    config = Config.build()
    logger.info(f'Starting {config.app_name}...')


if __name__ == '__main__':
    main()
