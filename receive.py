from ast import While
from cmath import e
import pika, sys, os
import asyncio

def connectToHost():
    try:
        parameters = pika.ConnectionParameters(host="localhost")
        return pika.BlockingConnection(parameters)
    except e: print('Connect to localhost encountered a problem')

def closeConnection(connection):
    try:
        connection.close()
    except Exception as e: print('Error:' + e)
    
def send(body):
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.basic_publish(exchange='e.messenger',
                                        routing_key= 'Hi',
                                        body="App2: " + body)
        closeConnection(connection)
        
    except Exception as e : print('Error:' + e)
        
def receive():
    connection = connectToHost()
    channel = connection.channel()
    channel.queue_declare(queue='q.messenger',
                            passive= False,
                            durable= True,
                            auto_delete= False,
                            arguments=None)

    def callback(ch, method, properties, body):
        print(body)
        # print(int(properties.priority))
        # print(properties)

    channel.basic_consume(queue='q.messenger', on_message_callback=callback, auto_ack=True)
    
    print(' [*] Waiting for messages. If you want send message press CTRL+C')
    channel.start_consuming()

# try:
#     receive()
# except KeyboardInterrupt:
#     your_message = input("Your message:")
#     send(your_message)
status =  True
while status == True:
    try:
        receive()
    except KeyboardInterrupt: 
        your_message = input("Your message:")
        send(your_message)

    