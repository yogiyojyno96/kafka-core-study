# Section 6 : Java 기반 Consumer 구현 실습 및 Consumer 내부 메커니즘 이해 - 03

### Consumer의 읽기 Offset Commit(커밋)과 중복 읽기 상황의 이해
__consumer_offsets에는 Consumer Group이 특정 topic의 파티 션별로 읽기 commit한 offset 정보를 가짐.

특정 파티션을 어느 consumer가 commit 했는지 정보를 가지지 않음 - 중복 읽기, 읽기 누락 발생의 원인

### Consumer의 Auto Commit(자동 커밋) 이해
- Auto Offset: 사용자가 명시적으로 코드로 commi을 기술하지 않아도 Consumer가 자 동으로 지정된 기간마다 commi을 수행
- Manual Offset: 사용자가 명시적으로 commit을 기술. Sync, Async 방식이 있음

### Auto Commit 적용 실습


### Auto Commit 적용 시 Consumer의 중복 읽기 상황 발생 실습


### Consumer의 동기 및 비동기 Manual Commit(수동 커밋) 이해
sync : 브로커에 commit 적용이 성공적으로 될 때까지 블로킹 적용
async : 브로커에 commit 적용이 성공적으로 되었음을 기다리지 않고(블로킹 하지 않음) 계속 메시지를 읽어옴.


### Consumer에서 토픽의 특정 파티션만 명시적으로 할당하기 구현 실습


### Consumer에서 토픽 특정 파티션의 특정 offset 부터 읽어오기 구현 실습


