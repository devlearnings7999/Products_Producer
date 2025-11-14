import os
import json
import random
import time
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

KAFKA_BROKER = os.getenv('KAFKA_BROKER')
PRODUCER_TOPIC = os.getenv('PRODUCER_TOPIC')
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL')
SASL_MECHANISM = os.getenv('SASL_MECHANISM')
SASL_USERNAME = os.getenv('SASL_USERNAME')
SASL_PASSWORD = os.getenv('SASL_PASSWORD')

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    security_protocol=SECURITY_PROTOCOL,
    sasl_mechanism=SASL_MECHANISM,
    sasl_plain_username=SASL_USERNAME,
    sasl_plain_password=SASL_PASSWORD,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_product_data():
    product_id = random.randint(100, 999)
    product_names = ['wireless headphones', 'cotton shirt', 'portable blender', 'mystery novel', 'running shoes']
    product_name = random.choice(product_names)
    return {
        'product_id': product_id,
        'product_name': product_name
    }

if __name__ == '__main__':
    while True:
        product_data = generate_product_data()
        print(f'Producing message: {product_data}')
        producer.send(PRODUCER_TOPIC, product_data)
        time.sleep(random.randint(1, 3))
