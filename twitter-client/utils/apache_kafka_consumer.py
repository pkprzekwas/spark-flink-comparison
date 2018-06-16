from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer('tw-app')
    for msg in consumer:
        print(msg)
