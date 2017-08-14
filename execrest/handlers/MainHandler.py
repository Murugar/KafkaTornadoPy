#!/usr/bin/python2.7

__name__ = 'MainHandler'

import json 
import time
from tornado import gen, web, httpclient
from kafka import KafkaConsumer

class MainHandler(web.RequestHandler):
    @web.asynchronous
    @gen.coroutine
    def get(self):
        consumer = KafkaConsumer('messages',
                                 group_id='my_group',
                                 bootstrap_servers=['localhost:9092'])

        
        client = httpclient.AsyncHTTPClient()
        self.write('some opening')

        print ("Consumed Start") 
        for message in consumer:
           
           print ("Consumed Msg -> '%s' on Topic -> '%s' with Offset -> %d" %
                  (message.value.decode('utf-8'), message.topic, message.offset))
           
                 
           self.write(message.value.decode('utf-8')) 

        self.write("Consumer Close") 
        consumer.close()

        
