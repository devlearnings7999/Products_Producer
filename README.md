# Products Producer

This project contains a Kafka producer that generates product data and sends it to a Kafka topic.

## Prerequisites

*   Kafka broker
*   Python 3.6+
*   `kafka-python` library
*   `.env` file with Kafka configuration

## Usage

1.  Install the required Python libraries:
    ```bash
    pip install kafka-python python-dotenv
    ```

2.  Configure the Kafka connection by editing the `.env` file with your Kafka broker address, username, password, and other settings.

    ```
    KAFKA_BROKER=<your_broker_address>
    PRODUCER_TOPIC=products_producer
    SECURITY_PROTOCOL=SASL_PLAINTEXT
    SASL_MECHANISM=SCRAM-SHA-512
    SASL_USERNAME=<your_username>
    SASL_PASSWORD=<your_password>
    ```

3.  Run the producer script:
    ```bash
    python product_producer.py
    ```

## Docker

1.  Build the Docker image:
    ```bash
    docker build -t products-producer .
    ```

2.  Run the Docker container, passing the environment variables:
    ```bash
    docker run -d --name products-producer \
       -e KAFKA_BROKER=<your_broker_address> \
       -e PRODUCER_TOPIC=products_producer \
       -e SECURITY_PROTOCOL=SASL_PLAINTEXT \
       -e SASL_MECHANISM=SCRAM-SHA-512 \
       -e SASL_USERNAME=<your_username> \
       -e SASL_PASSWORD=<your_password> \
       products-producer
    ```