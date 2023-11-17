from stompest.config import StompConfig
from stompest.sync import Stomp
from stompest.protocol import StompSpec
import random
import string
import uuid
import json

class ActiveMQ:
    def __init__(self) -> None:
        self.CONFIG = StompConfig(uri='ssl://'+'localhost'+':61613',version='1.2')

    def message_listener(self,queue_name,id):
        queue =  '/queue/' + queue_name
        client = Stomp(self.CONFIG)
        client.connect(heartBeats=(0,1000))
        token =client.subscribe(queue,{StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL,"id":id,"activemq.prefetchSize": 1})

        frame = None
        random_uuid = None
        while True:
            random_uuid = self.gen_random_uuid()
            frame= client.receiveFrame()
            input_json = self.fetch_input_message(frame)
            client.ack(frame)
        client.disconnet()
    
    def generate_random_pk(self,no_of_characters = 6):
        try:
            res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k = no_of_characters))
            return res
        except Exception as err:
            raise Exception(err)
    

    def gen_random_uuid(self) -> str:
        """
        This method help to produce random uuid number
        @return: random uuid number
        """
        random_uuid = uuid.uuid4()
        return str(random_uuid).replace('-', '')
    
    def fetch_input_message(self, frame):
        input_json = json.loads(frame.body.decode())
        return input_json 

# if  __name__ == '__main__':
#     objMq = ActiveMQ()
#     objMq.message_listener('dcb-producer-test',4400)