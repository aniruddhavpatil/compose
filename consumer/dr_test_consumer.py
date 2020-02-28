from kafka import KafkaConsumer
import time
# time.sleep(10)
bootstrap_servers = ['localhost:9092']
topicName = 'test'
consumer = KafkaConsumer(
	topicName,
	bootstrap_servers = bootstrap_servers,
	auto_offset_reset='earliest',
    enable_auto_commit=True,
	# value_serializer=lambda m: json.dumps(m).encode('ascii')
	)

# try:
print("Created kafka consumer")
for i,message in enumerate(consumer):
	print(i, message.value)
# except:
# 	print("I fucked up")
# 	pass
