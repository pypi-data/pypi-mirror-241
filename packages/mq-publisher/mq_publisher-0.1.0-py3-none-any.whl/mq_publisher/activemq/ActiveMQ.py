from stompest.sync import Stomp
from stompest.config import StompConfig

class ActiveMQ:
    def __init__(self) -> None:
        try:
            self.CONFIG = StompConfig(uri='ssl://'+'localhost'+':61613',version='1.2')
        except Exception as e:
            pass
    
    def send_message(self, queue_name,message):
        try:
            queue = '/queue/' + queue_name
            client = Stomp(self.CONFIG)
            client.connect()
            client.send(queue, message.encode())
            client.disconnect()
        except Exception as e:
            pass
