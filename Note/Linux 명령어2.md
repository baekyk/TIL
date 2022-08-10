	• echo
		○ 화면에 글자 출력
		○ -n : 뉴라인 제외
		○ -e : Escape 코드 지원
		○ -E : Escape 코드 미지원

	• redirection 
		○ output 을 다른 장치로 보냄
		○ >: output 출력, 덮어씀
		○ >>: append
		○ 2>: stderr 출력
		○ 2>& stderr 값을 보냄
		○ < : stdin , stdin 지원 여부에 따라 작동
		○ << : delimiter, 이후 입력값이 나올때까지 입력받음
			§ cat << eof (eof 입력 할때까지 입력받음)
			§ ex ) cat << eof > hello.txt
		
	• pipe (|)
		○ 출력값을 프로세스간 전달
		○ | grep  : output 내에서 검색
		○ | wc -l : output 내 줄 개수 확인
		○ 다중 파이프 가능

	• history
		○ shell 내 명령어 기록 ( 최근 1000개, 총 2000개)

	• path
		○ 환경변수
		○ path의 순차적으로 검색됨

	• which
		○ file 위치
		○ 내가 실행하는 바이너리 위치
		
		
	• alias
		○ 단축명령어
		○ alias ..="cd .."
		○ alias en="LANGUAGE=en"

	• shebang
		○ 해당 shell 스크립트의 속성을 첫줄에 정의
		○ #!/bin/bash
		○ #!/usr/bin/python
