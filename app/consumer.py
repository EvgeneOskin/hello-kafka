from kafka import KafkaConsumer


consumer = KafkaConsumer('hello', bootstrap_servers='kafka')

for msg in consumer:
    print (msg)
