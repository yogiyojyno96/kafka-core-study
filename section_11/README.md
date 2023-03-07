# 섹션 11. Producer와 Consumer의 Custom 객체 직렬화/역직렬화

confluent-kafka-python 은 객체 직렬화/역직렬화 담당하는 class를 지정해서 [producer](https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/avro_producer.py#L116-L142), [consumer](https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/avro_consumer.py#L83-L112)를 생성함

아님 처음에 설정한 serializer 로 받아올 수 있도록 할 수 있습니다 - [DeserializingConsumer](https://github.com/yogiyo/logistics-schedule-api/blob/code-review/rider_schedule/engine/services/confluent_kafka_client.py#L35-L48) class 를 사용하면 됩니다

schema registry 실습 해보면 좋을것 같습니다 - 추후 진행