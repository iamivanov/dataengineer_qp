from kafka import KafkaConsumer
from datetime import datetime
import pg8000
from json import loads
import json

dbname = 'postgres'
user = 'ivanov'
password = 'r2q4e'
host = '192.168.77.21'
port = 5432

try:
    conn = pg8000.connect(
        database = dbname,
        user = user,
        password = password,
        host = host,
        port = port
    )

    consumer = KafkaConsumer(
        'lab10_ivanov',
        bootstrap_servers='vm-strmng-s-1.test.local:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='lab10_ivanov',
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    
    cursor = conn.cursor()
    insert_sql = "INSERT INTO ivanov_traps_raw VALUES (%s, %s, %s)"
    
    for message in consumer:
        print(message.value)
        cursor.execute(insert_sql, (message.value, datetime.now(), datetime.today()))
        conn.commit()
        #time.sleep(1)

finally:
    consumer.close()
    conn.close()
