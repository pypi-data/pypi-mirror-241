import json
from kafka import KafkaProducer
# from kafka.errors import KafkaError

from kafka_message.model.producer_model import ProducerModel


class KafkaMessageProducer:
    def __init__(self, bootstrap_servers: str, security_protocol: str, ssl_cafile: str, 
                 sasl_mechanism: str, sasl_plain_username: str, sasl_plain_password: str):
        self.bootstrap_servers = bootstrap_servers
        self.security_protocol = security_protocol
        self.ssl_cafile = ssl_cafile
        self.sasl_mechanism=sasl_mechanism
        self.sasl_plain_username=sasl_plain_username
        self.sasl_plain_password=sasl_plain_password


    def send_message(self, topic: str, model: ProducerModel):
        try:
            producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,     
                                    security_protocol=self.security_protocol,
                                    ssl_cafile=self.ssl_cafile,
                                    sasl_mechanism=self.sasl_mechanism,
                                    sasl_plain_username=self.sasl_plain_username,
                                    sasl_plain_password=self.sasl_plain_password,

                                    compression_type='gzip', 
                                    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                    key_serializer=lambda v: json.dumps(v).encode('utf-8')
                                    )
             
            producer.send(topic, model.value, model.key, model.headers)           

            print(f"Message sent to topic '{topic}'")
            return True, f"Message sent to topic '{topic}'"
        except Exception as e:
            # log.error(e, exc_info=True)
            print(f"Failed to send message to topic '{topic}': {str(e)}")
            return False, f"Failed to send message to topic '{topic}': {str(e)}"
        finally:
            producer.close()
