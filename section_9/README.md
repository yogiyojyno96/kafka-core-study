# 섹션 9. 멀티 노드 카프카 클러스터


## 멀티 노드 카프카 클러스터 개요 및 분산 시스템 장단점

성능 및 가용성 향상에 좋다고 하네요~
replication 설정을 위해 최대한 가용성을 보장합니다.

## 3개의 멀티 브로커로 카프카 구성하기
3개의 브로커를 설정해보자
각각의 브로커는 다른 properties 로 설정
다른 포트를 가짐
-> docker 로 진행 해보자.

## 멀티 브로커 카프카에서 여러 개의 파티션을 가지는 다중 복제 토픽 만들기
3개 다 살아있을때 topic partition 3개 생성하면 각각 1개 씩 잘 생성 됨
2개만 살아있을 때 3개 생성하면 둘중 하나에 2개, 남은거 하나에 1개 생성됨 - 생성 당시에 leader가 지정함

## 카프카 Replication(복제)와 리더(Leader)/팔로워(Follower) 이해
repflication factor가 3이면 원본 + 복제 = 3 을 의미함
이 값은 토픽 생성 시 설정 할 수 잇음
이 값은 브로커의 수를 넘을 수 없음

replication 의 동작은 토픽 내의 개별 파티션들을 대상으로 적용

produce, consumer는 leader 에만 쓰고 읽음

멀티파티션인 경우 리더는 파티션 별로 존재함

ISR? - 잘 따라오고 있는 repflication 을 의미

## 멀티 브로커 환경에서 Producer의 bootstrap.servers 설정 이해
멀티 브로커가 되면 각 브로커 별로 포트가 다 달라지는데 어떻게 함?, 다 넣어주면 됨
bootstrap.servers 적는 서버 주소는 broker의 metadata를 가져올 서버 주소를 적는 것
하나만 접속하면 모든 멀티 브로커에 대한 메타 데이터를 가져옴 - 그럼 하나만 적으면 되는거 아닌가요?
- 작성해둔 브로커가 죽었을 가능성도 있기 때문에 다 적어두는 것이 좋습니다.

## 주키퍼(Zookeeper)와 컨트롤러(Controller) 브로커의 이해
zookeeper 의 역할
- 컨트롤러 브로커는 파티션 리더를 선출합니다.
- kafka 클러스터내 Broker의 Membership 관리
- topic 에 대한 정보 관리

## ISR(In-Sync_Replicas)의 이해
3번이 죽어도 repflication 은 그대로 있고 isr 만 줄어들음 왜?

follower 누구든 leader 가 될 수 있음 - 단 ISR 인 경우 - 건강한 브로커를 관리하고 있는 거
지속적으로 따라오지 못하고 있다고 판단되면 바로 ISR에서 탈락시킴

판단 조건
1. replica.lag.time.max.ms 로 설정 된 기간 내에 leader의 메세지를 지속적으로 가져가야함
2. 최신 offset 번호 비교

## min.insync.replicas 설정에 따른 Producer 전송 이해
acks=all 으로 성공적으로 메세지를 보낼 수 있는 최소한의 ISR 브로커 개수를 의미


## Preferred Leader Election 이해 및 실습


## Unclean Leader Election 이해 및 실습

