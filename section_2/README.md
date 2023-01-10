# Section 1: 섹션 2. Java 기반 Producer 구현 실습 및 Producer 내부 메커니즘 이해 - 01

### Java 기반에서 Producer 구현하기 - 01
setting topic 생성
```shell
[appuser@broker ~]$ kafka-topics --bootstrap-server localhost:9092 --create --topic simple-topic
Created topic simple-topic.
```
 
producer 생성해서 record 생성 후 전송 시도
- 참고 https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/avro_producer.py

진행한 코드 : section_2/simple_producer.py, section_2/settings/py

```shell
Usage: <bootstrap-brokers> : 127.0.0.1:9092 <topic> simple-topic
test

% Message delivered to simple-topic [0] @ 0
test2
% Message delivered to simple-topic [0] @ 1

% Message delivered to simple-topic [0] @ 2

% Message delivered to simple-topic [0] @ 3
test3
% Message delivered to simple-topic [0] @ 4
```

### Java 기반에서 Producer 구현하기 - 02

Todo 

### Producer Java 클라이언트 API 내부를 Intellij Debugger를 이용하여 살짝 뜯어보기

Todo 

### Producer의 메시지 동기화 전송 구현

Todo 

### Callback을 이용한 Producer의 메시지 비동기화 전송 이해

Todo 

### Producer의 메시지 비동기화 전송 구현

Todo 

### Producer에서 키(Key)값을 가지는 메시지 전송 구현

Todo 

### Producer에서 키(Key) 타입의 변경 및 Custom Callback 구현

Todo 

### 피자 주문 시뮬레이션 Producer 구현: 피자 주문 메시지 생성

Todo 

### 피자 주문 시뮬레이션 Producer 구현: 피자 주문 Producer 구현 - 01

Todo 

### 피자 주문 시뮬레이션 Producer 구현: 피자 주문 Producer 구현 - 02

Todo 

