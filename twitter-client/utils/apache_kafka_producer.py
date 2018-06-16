from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')


for _ in range(100):
    producer.send('tw-app', b'twitter-api-example')
