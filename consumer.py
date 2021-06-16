#!/usr/bin/env python
import pika, sys, os,logging


# Establishing RabbbitMQ connection

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

# callback method to get the published data

    def callback(ch, method, properties, body):
       var1= body
       print(var1)

	#creating log file

       LOG_FILENAME = "logfile.log"
       for handler in logging.root.handlers[:]:
       	logging.root.removeHandler(handler)
       logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s', datefmt='%m/%d/%Y%I:%M:%S %p')    
       logging.info('CURRENT CPU STATUS')
       logging.getLogger("pika").setLevel(logging.WARNING)
       logging.info(var1)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
