# Section 3: Java 기반 Producer 구현 실습 및 Producer 내부 메커니즘 이해 - 02

### acks 값 설정에 따른 Producer의 전송 방식 차이 이해

ask 0 : 브로터가 메세지를 받았는지 못받았는지 상관 없이 바로 완료 처리

ask 1 : 메인 브로커에 저장 완료 되었는지만 확인

asks all : replicator 전부에 ack 수락 될 때 까지 대기 - 너무 느림, 하지만 확실

Callback 기반의 async에서도 동일하게 acks 설정에 기반하여 retry가 수행됨

Callback 기반의 async에서는 retry에 따라 Producer의 원래 메시지 전송 순서와
Broker에 기록되는 메시지 전송 순서가 변경 될 수 있음.


### Producer의 메시지 배치 전송 내부 메커니즘 - Record Batch와 Record Accumulator 이해

Record Batch? : message를 send 하면 바로 kafka broker로 가는 것이 아니라 내부 
메모리에서 토픽 파티션에 따라 Record Batch 단위로 묶인 뒤 전송 됨
- 메모리 크기는 buffer.memory 설정을 통해 조정 가능


Record Accumulator ? :Partitioner에 의해서 메시지 배치가 전송이 될 토픽과 Partition에 따라 저장되는 KafkaProducer 메모리 영역

Sender Thread는 Record Accumulator에 누적된 메시지 배치를 꺼내서 브로커로 전송

KafkaProducer의 Main Thread는 send( ) 메소드를 호출하고 Record Accumulator 에 데이터 저장하고 Sender Thread는 별개로 데이터를 브로커로 전송

### Producer의 메시지 배치 전송 내부 메커니즘 - linger.ms와 batch.size 파라미터 고찰

linger.ms : Sender Thread로 메시지를 보내 기전 배치로 메시지를 만들어서 보내기위한 최대 대기 시간

linger.ms를 0보다 크게 설정하여 Sender Thread가 하나의 Record Batch를 가져갈 때 일정 시간 대기하여 Record Batch에 메시지를 보다 많이 채울 수 있도록 적용

전반적인 Producer와 Broker간의 전송이 느리다면 linger.ms 를 높여서 메시지가 배치로 적용될 수 있는 확률을 높이는 시도를 해볼만함


### Producer의 max.in.flight.requests.per.connection 파라미터와 배치 메시지의 전송순서 이해

Todo

### 최대 한번전송, 적어도 한번전송, 정확히 한번전송 이해

최대 한번전송 : producer가 ack를 기다리지 않고 계속 전송 - 중간에 메세지 소실 될 수 있음

적어도 한번전송 : ack 받은 후 메세지 전송. 메세지 소실은 없지만 중복 전송할 수 있음

정확히 한번전송(중복 없이 전송(idempotence))
- Producer는 브로커로 부터 ACK를 받은 다음에 다음 메시지 전송하되, Producer ID와 메시지 Sequence를 Header에 저장하여 전송
- 메시지 Sequence는 메시지의 고유 Sequence번호. 0부터 시작하여 순차적으로 증가. Producer ID는 Producer가 기동시마다 새롭게 생성
- 브로커에서 메시지 Sequece가 중복 될 경우 이를 메시지 로그에 기록하지 않고 Ack만 전송.
- 브로커는 Producer가 보낸 메시지의 Sequence가 브로커가 가지고 있는 메시지의 Sequence보다 1만큼 큰 경우에만 브로커에 저장

`Idempotence 적용 후 성능이 약간 감소(최대 20%)할 수 있지만 기본적으로 idempotence 적용을 권장`

### idempotence(멱등성) 기반 중복 없이 전송 이해

Todo

### Producer에 idempotence(중복 없이 전송) 설정 및 설정 시 유의 사항

ask 1 로 바꾸면 기동 실패할 수 있음 - 설정 조심히 변경할 것
