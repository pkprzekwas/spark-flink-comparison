from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer('twitter_stream')
    for msg in consumer:
        print(msg)
