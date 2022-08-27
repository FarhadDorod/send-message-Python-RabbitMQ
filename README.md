# This is a sample of RabbitMQ based on python and Operation system is windows

# What is RabbitMQ?

- it is software where queues are defined, to which applications connect in order to transfer a message or messages.

# RABBITMQ AND SERVER CONCEPTS

- **Producer:** Application that sends the messages.
- **Consumer:** Application that receives the messages.
- **Queue:** Buffer that stores messages.
- **Message:** Information that is sent from the producer to a consumer through RabbitMQ.
- **Connection:** A TCP connection between your application and the RabbitMQ broker.
- **Channel:** A virtual connection inside a connection. When publishing or consuming messages from a queue - it's all done over a channel.
- **Exchange:** Receives messages from producers and pushes them to queues depending on rules defined by the exchange type. To receive messages, a queue needs to be bound to at least one exchange.
- **Binding:** A binding is a link between a queue and an exchange.
- **Routing key:** A key that the exchange looks at to decide how to route the message to queues. Think of the routing key like an address for the message.
- **AMQP:** Advanced Message Queuing Protocol is the protocol used by RabbitMQ for messaging.
- **Users:** It is possible to connect to RabbitMQ with a given username and password. Every user can be assigned permissions such as rights to read, write and configure privileges within the instance. Users can also be assigned permissions for specific virtual hosts.
- **Vhost, virtual host:** Provides a way to segregate applications using the same RabbitMQ instance. Different users can have different permissions to different vhost and queues and exchanges can be created, so they only exist in one vhost.

# TYPES OF EXCHANGES

- **Direct:** The message is routed to the queues whose binding key exactly matches the routing key of the message. For example, if the queue is bound to the exchange with the binding key pdfprocess, a message published to the exchange with a routing key pdfprocess is routed to that queue.
- **Fanout:** A fanout exchange routes messages to all of the queues bound to it.
- **Topic:** The topic exchange does a wildcard match between the routing key and the routing pattern specified in the binding.
- **Headers:** Headers exchanges use the message header attributes for routing.

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
2. **send.py :** This part responsible is sending messages to Exchange and queue. Messages are not published directly to a queue; instead, the producer sends messages to an exchange. An exchange is responsible for routing the messages to different queues with the help of bindings and routing keys. A binding is a link between a queue and an exchange.
3. **receive.py :** This part responsible is only get messages 


**CloudAMQP(https://www.cloudamqp.com/plans.html) is a hosted RabbitMQ solution, meaning that all you need to do is sign up for an account and create an instance. You do not need to set up and install RabbitMQ or care about cluster handling, CloudAMQP will do that for you. CloudAMQP can be used for free with the plan little lemur.**
