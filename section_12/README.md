# 섹션 12. 토픽의 세그먼트(Segment) 관리

카프카의 로그는 세그먼트에 저장됨

메시지 Segment는 File기반이므로 특정 offset의 데이터를 파일에서 읽기 위해서는 시작 File Pointer에서 얼마만큼의 byte에 위치해 있는지 알아야함.
- 해당 정보를 저장하는 index 파일이 있음
- 무한한 메세지를 각각 index 로 지정할 수 없기에 일정 범위의 segment의 offset 마다 index 로 관리됨
