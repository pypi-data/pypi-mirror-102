# Overview
PyMom is a Python framework that enables the creation of event-driven systems leveraging messaging systems like Kafka and Google's Cloud Pub/Sub.

# Installation
This repo can be installed with pip:

```
pip3 install pymom
```

# Configuration
PyMom expects the environment variable ```PYMOM_CONFIG_FILE``` to be set to the name of the configuration file.  This file specifies the Kafka bootstrap brokers and Zookeeper servers in this format:

```
[DEFAULT]
kafka-bootstrap-brokers = localhost:9092
zookeeper-servers = localhost:2181
```

# Message Formats
The current implementation of PyMom uses the PyMomMessage format.  All messages on Kafka are in JSON format and must include at least two elements:

* ```id``` is a key that correlates multiple related messages.  It is used for partitioning Kafka topics.
* ```payload``` is the content of the message.  It can be any valid JSON.

# Producing Messages
PyMom provides access to a class for writing messages to a Kafka topic.  ```PyMomTestProducer.py``` demonstrates how to use it:

```
pymom = PyMom()
producer = pymom.producer('test.pymom.consume')  # The topic name.
producer.write(sys.argv[1],sys.argv[2])  # The ID and payload.
```

# Consuming Messages
To receive messages from Kafka, a class must derive from ```PyMomAbstractConsumer``` and implement the ```on_message``` method.  The class must then be registered with PyMom.  ```PyMomTestConsumer.py``` demonstrates how to do this:
```
class PyMomTestConsumer(PyMomAbstractConsumer):
    def __init__(self,pymom):
        self.pymom = PyMom()
        self.producer = self.pymom.producer('test.pymom.produce')

    def on_message(self,message):
        """ Process messages. """
        id = message['id']
        payload = message['payload']
        print("Received message:  ({}) {}".format(id,payload))
        try:
            self.producer.write(id,payload)
            print("Wrote message.")
        except Exception as error:
            print("Unable to send message:  {}".format(error))


if __name__ == "__main__":
    pymom = PyMom()
    consumer = PyMomTestConsumer(framework)
    pymom.register(consumer,'PyMomTestConsumerGroup','test.pymom.consume')
    pymom.run()
    
    print("PyMomTestConsumer terminated.")
    sys.exit(0)
```
```on_message``` can either return normally or throw one of two exceptions.  If a recoverable error (e.g an external API is temporarily unavailable) occurs, throw ```PyMomRecoverableError```.  If an unrecoverable error (e.g. the message format is invalid) occurs, throw ```PyMomUnrecoverableError```.  In both cases, the error is logged.  In the case of a recoverable error, the message will be retried.  In the case of an unrecoverable error, processing will continue with the next message.

