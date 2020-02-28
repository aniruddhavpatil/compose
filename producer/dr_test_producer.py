from kafka import KafkaProducer
import time
# time.sleep(10)
bootstrap_servers = ['localhost:9092']
topicName = 'test'
producer = KafkaProducer()
for i in range(10):
	ack = producer.send('test', str(i).encode())
producer.flush()