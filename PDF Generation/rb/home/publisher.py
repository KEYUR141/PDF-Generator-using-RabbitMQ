import pika
import random
import json

def publish_message(message):
    params = pika.URLParameters('amqps://poaxryvt:XcOKhmp9oiEG9n_huXHnqXvg2lJzLNHJ@puffin.rmq2.cloudamqp.com/poaxryvt')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="my_queue")
    message = json.dumps(message)
    channel.basic_publish(
        exchange = '',
        routing_key="my_queue",
        body = message
    )
    print(f"Messages Publishes {message}")
    connection.close()