from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='kafka')

for _ in range(100):
    producer.send('hello', b'some_message_bytes')
