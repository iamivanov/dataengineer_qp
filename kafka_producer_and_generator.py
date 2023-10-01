from kafka import KafkaProducer
import time
import json
import csv
from random import randint, random

try:
    producer = KafkaProducer(
        bootstrap_servers='vm-strmng-s-1.test.local:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    #csv на основе которых генирируются сообщения в кафку
    with open('file.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            print(', '.jpin(row))


    for i in range(1000):
        #выберем клиента случайным образом
        client = clients[randint(0,len(clients)-1)]
        #определим приоритет
        a = random()
        if 0.75 < a <= 0.95:
            priority = 1
        elif 0.95 < a:
            priority = 2
        else:
            priority = 0


        #сгенирируем дату и время
        opened = str(randint(1,28))+'.'+str(randint(1,12))+'.'+str(randint(2022,2024))+' '+time.strftime('%H:%M', time.localtime())


        #создадим сообщение
        message = {'client' : client, 'opened': opened, 'priority': priority}


        print(message)
        producer.send('lab10_ivanov', value = message)
        print('message sent')
        #time.sleep(1)


finally:
    producer.close()
