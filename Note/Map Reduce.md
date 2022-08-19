	• 2004년 구글에서 발표한 Large Cluster에서 Data Processing을 하기위한 알고리즘
	• Key - Value 구조가 알고리즘의 핵심
	• 데이터가 분산처리가 가능한 연산에 적합
	• HDFS에 분산 저장돼 있는 데이터를 병렬로 처리하여 취합
	• Map function과 Reduce function으로 구성
	• 같은 key는 같은 server로 reduce

	• Map 
		○ key값을 기준으로 병렬 분산
		○ 같은 key값을 가지고 있는 파일끼리 모여 reduce로 전달
	• Reduce
		○ 취합 한 key에 대한 list 생성
	• 작은 양의 데이터도 처리 시간이 오래걸림 -> 대용량 처리에 적합
