	• NameNode - Hadoop master daemon name
		○ 데이터의 위치, 형식 보관 (meta data)
		○ Datanode로 부터 block 리포트 받음
	• SNN(Sub Name Node)
		○ 1시간 or name node의 edits 로그가 일정 이상 쌓이면 edit 와 fsimage 복사해와서 merge 후 다시 전송
		○ name node의 edit 사이즈, 메모리를 일정하게 유지
		○ standby 구조가 아님
	• DataNode - slave node
		○ 실제 데이터가 저장됨
		○ 주기적으로 block 리포트
	
	• 큰 파일을 여러개의 Block으로 나누어 저장
	• Slave node의 쉬운 확장 가능
	• 데이터 복제본 자동 관리
	• 한번 쓰고 많은 읽기가 있는 오퍼레이션에 최적화
	
	• Block
		○ 하나의 파일을 여러개의 block으로 저장
		○ 64MB or 128MB 등등 크기로 저장
		○ 탐색 비용을 최소화하기 위해 block이 큼
		○ 한 block을 3 copy 각각 저장함(default)
		
	• 장애 발생
		○ Data node -> Name node 3초마다 heart beat 송신
		○ Data node에 문제가 발생하면 (under replicated)
		○ name node에서 해당 data node 외의 다른 data node의 데이터를 다른 data node에 복사하도록 지시 (3 copy 유지)
		○ 장애 data node가 복구 되면 (over replicated) 4개 중 하나를 삭제함 

	• HDFS 2.0
		○ HDFS 1.0 은 NameNode가 전체 시스템의 SPOF(single point of failure)
		○ name node 장애를 대비해 JN에 fsimage와 edit을 저장
		○ Failover Controller : name node가 정상 작동 하는지 감시
		○ 2가지 방식의 HA 지원
		
	• HDFS 3.0
		○ Erasure coding : 3배의 disk가 아닌 2배의 disk를 사용해 효율적인 용량 활용

	• HDFS Federation
		○ 하나의 name node에서 관리하는 파일, 블록이 많아지면 물리적 한계
		
