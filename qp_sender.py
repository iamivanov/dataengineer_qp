from kafka import KafkaProducer
import json
import re
import time

try:
    producer = KafkaProducer(
        bootstrap_servers='vm-strmng-s-1.test.local:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    #read sova_trap.csv
    
    with open('../trap_jsons.csv', 'r') as file:
        lines = (ln for ln in file)
        for raw in lines:
            print('new line\n')
            #print(raw)
            if re.match(r'^\{', raw):
                trap = json.loads(raw)
                trap.pop('device_name')
                trap.pop('collector')
                print(trap)
                producer.send('lab10_ivanov', value = trap)
                print('message sent')
                #time.sleep(10)

finally:
    producer.close()
