import pika, sys, os

def connectToHost():
    try:
        parameters = pika.ConnectionParameters(host="localhost")
        return pika.BlockingConnection(parameters)
    except Exception as  e: print('Error:' + e)
    
def closeConnection(connection):
    try:
        connection.close()
    except Exception as e: print('Error:' + e)

def send(body):
    connection = connectToHost()
    try:
        channel = connection.channel()
        result = channel.basic_publish(exchange='e.messenger',
                                        routing_key= 'Hi',
                                        body="App1: " + body)
        closeConnection(connection)
        
    except Exception as e : print('Error:' + e)
    main()

def main():
    app1_message = input("You:")
    send(app1_message)

print("Your name is App1")
main()    
    