import json
from multiprocessing import connection
import queue
from ast import Pass
from asyncio.windows_events import NULL
from cmath import e
from gc import callbacks
from multiprocessing.connection import Connection
from os import lseek
from sqlite3 import connect
from tkinter.messagebox import NO
from typing import Any

import pika

def connectToHost():
    try:
        parameters = pika.ConnectionParameters(host="localhost")
        # parameters = pika.URLParameters(url='amqps://unbvroga:3TX16oOFhyAVGofHs4KeO09kW2yc6IFK@fly.rmq.cloudamqp.com/unbvroga')
        return pika.BlockingConnection(parameters)
    except Exception as  e: print('Error:' + e)

def createExchange():
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.exchange_declare(exchange='e.messenger', 
                            exchange_type='direct', 
                            passive= False,
                            durable=True,
                            auto_delete=False, 
                            internal=False,
                            arguments=None)
        closeConnection(connection)
        print("The Exchange was created successfully")
    except Exception as e: print('Error:' + e)

def createQueue():
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.queue_declare(queue='q.messenger',
                            passive= False,
                            durable= True,
                            auto_delete= False,
                            arguments=None)
        closeConnection(connection)
        print("The Sum Queue was created successfully")
    except Exception as e: print('Error' + e)

def bindingQueueToExchange():
    connection = connectToHost()
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.queue_bind(queue='q.messenger' ,
                            exchange='e.messenger',
                            routing_key='Hi')
        closeConnection(connection)
        print("The binding was successfully")
    except Exception as e: print('Error' + e)
    
def closeConnection(connection):
    try:
        connection.close()
    except Exception as e: print('Error:' + e)

def deleteExchangeAndQueue():
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.exchange_delete(exchange="e.calculate", if_unused= False)
        channel.queue_delete(queue="q.sum")
        closeConnection(connection)
    except: print('Delete Exchange and Queue encountered a problem')
    
print("//***************************************************\\")
print("1-Create Exchange")
print("2-Create Queue")
print("3-Binding Queue To Exchange")
print("4-Delete Queue and Exchange")
print("//***************************************************\\")
selectedNumber = input("Please select your item then press Enter:")

if selectedNumber == '1': createExchange()
if selectedNumber == '2': createQueue()
if selectedNumber == '3': bindingQueueToExchange()
if selectedNumber == '4': deleteExchangeAndQueue()

