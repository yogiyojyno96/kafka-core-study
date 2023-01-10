# Section 2: Java 기반 Producer 구현 실습 및 Producer 내부 메커니즘 이해 - 01

### python 기반에서 Producer 구현하기

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

producer에서 send 한다고 바로 메세지가 전송되지 않음 왜? 나중에 말해줌
flush를 사용해야 버퍼에 있는 값을 실제로 전송함

잘 전송되었는지 확인

```shell
[appuser@broker ~]$ kafka-console-consumer --bootstrap-server localhost:9092 --topic simple-topic --property print.key=true --property print.value=true --from-beginning
null    test
null    
null    test2
null    
null    
null    test3
```

### Producer의 메시지 동기화 전송 구현

기본적으로는 비동기 처리
그럼 순서 보장이 안되는데? - 하고싶음 동기로 구현하면 됨
Ack 받은 후 다음 메시지를 전송하도록 구현하면 됨 - 그럼 전송된 메세지의 정보는? callback 함수로 가져올 수 있음

동기로는 어떻게 함? - produce 하고 바로 poll 하면 되나? - 아님 produce 하고 flush 하면 되는듯

### Callback을 이용한 Producer의 메시지 비동기화 전송 이해

아하 그렇구나

### Producer의 메시지 비동기화 전송 구현

confleunt kafka producer는 sync 로 따로 구현하는 방법이 없는것 같아서 더 찾아봐야 할듯
우선 callback 함수 선언해서 비동기 처리만 해봄

### Producer에서 키(Key)값을 가지는 메시지 전송 구현

왜 키값을 지정해서 전송하는가? - 파티션 내 순서보장을 위해 키 값을 지정함

### Producer에서 키(Key) 타입의 변경 및 Custom Callback 구현

Todo

### 피자 주문 시뮬레이션 Producer 구현: 피자 주문 메시지 생성

Todo

### 피자 주문 시뮬레이션 Producer 구현: 피자 주문 Producer 구현 - 01

Todo

### 피자 주문 시뮬레이션 Producer 구현: 피자 주문 Producer 구현 - 02

Todo 

