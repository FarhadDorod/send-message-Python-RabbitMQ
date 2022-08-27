# send-message-Python-RabbitMQ
This is a sample of RabbitMQ based on python and Operation system is windows

# What is RabbitMQ?

- it is software where queues are defined, to which applications connect in order to transfer a message or messages.

# When and why should you use RabbitMQ?

- Message queueing allows web servers to respond to requests quickly instead of being forced to perform resource-heavy procedures on the spot that may delay response time. Message queueing is also good when you want to distribute a message to multiple consumers or to balance loads between workers.

# How to get start?

- Downloading and Installing RabbitMQ from https://www.rabbitmq.com/download.html
- After installing you should enable RabbitMQ management UI on Windows by insert "C:\Program Files\RabbitMQ Server\rabbitmq_server-3.8.0\sbin>rabbitmq-plugins.bat enable rabbitmq_management" on windows command line.
- Then RabbitMQ management UI are available on "http://localhost:15672". The default administrator username and password are guest and guest.
- Install pika on Python from https://pika.readthedocs.io/en/stable/index.html. Pika is a pure-Python implementation of the AMQP 0-9-1 protocol including RabbitMQ’s extensions.
- Now every thing is ok.

# This project has three parts:
1. **configuration.py :** In this part you can create Exchange and queue after then binding them and also if you want you can delete them
2. **send.py :** This part responsible is sending messages to Exchange and queue 
3. **receive.py :** This part responsible is only get messages 
