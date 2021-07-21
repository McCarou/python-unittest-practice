import pika

class RabbitMqModule():

    def __init__(self, host=None):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host)) if host else None
    
    def publishMessage(self, exchange='',
                      routing_key='',
                      body=''):
        channel = self.connection.channel()
        channel.basic_publish(exchange=exchange,
                      routing_key=routing_key,
                      body=body)
