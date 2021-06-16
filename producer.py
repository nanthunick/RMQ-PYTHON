#!/usr/bin/env python
import pika

# Importing the modules for CPU usage
import os
import psutil

#Calculating CPU load
load1, load5, load15 = psutil.getloadavg()

cpu_usage = (load15/os.cpu_count()) * 100



# Establishing RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Declaring a RabbitMQ queue
channel.queue_declare(queue='hello')


# Publishing the CPU status 
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=str(cpu_usage))
print(" [x] Sent 'CPU status!'")

connection.close()
