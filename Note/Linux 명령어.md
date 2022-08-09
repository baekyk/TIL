	• cat
		○ 파일 내용 보여주기
		○ cat -e /etc/passwd : 줄 맨 뒤에 $ (히든 공백 확인)
		○ car -n /etc/passwd : 줄 번호 출력
		
	• W
		○ 서버 접속 확인
		○ w | wc -l
		○ 서버 접속 중인 사람 수 확인
		
	• sudo lastb | wc -l
		○ 해킹 시도 수 확인
		
	• ls
		○ ls -al
		○ 숨겨진 파일까지 자세하게 출력
		
	• touch
		○ 파일 만들기
		○ touch hello.txt
		
	• echo
		○ 화면에 출력
		○ echo “hello”
		○ echo “hello” > hello.txt
		○ hello를 hello 텍스트에 저장
		
	• more
		○ cat 대신에 쓸 수 있는 출력
		○ more hello.txt
		
	• less
		○ more 보완하여 위 아래로 움직일 수 있음
		○ less hello.txt
		○ more보다 속도 빠름
		
	• rm
		○ 파일 삭제
		○ rm hello.txt
		
	• mkdir
		○ 폴더 만들기
		○ mkdir dir1
		
	• rmdir
		○ 폴더 지우기
		○ rmdir dir1
		
	• cd
		○ 자신의 위치 변경
		○ cd ~/  :   홈으로 돌아가기
		○ cd -     :  이전 위치로 돌아가기
		
	• mv
		○ 파일 이동
		○ mv dir2 dir3
		
	• ln -s
		○ ln -s hello.txt hellosym
		○ symbolic link
		○ 링크파일
		○ 바로가기를 만드는 것
		○ 용량을 작게 차지함
		○ 웹 서버 만들때 자주 사용
		○ ls -il 로 inode 확인 가능
	
		
	• ln
		○ ln hello2.txt hello3.txt
		○ 하드링크
		○ 시스템 내부적으로 동일한 파일임
		
	• file
		○ 어떤 파일인지 속성을 알려줌
		○ file hello.txt
		
	• whoami
		○ 내가 누구인지 확인
		
	• sudo
		○ 슈퍼유저의 권한을 수행
		○ 잠시 root권한을 가져와서 실행
		
	• useradd
		○ 그룹에 유저 추가
		○ useradd -aG user1 sudo
		○ user1을 sudo 그룹에 추가
		
	• chmod
		○ 소유자/그룹/그외 ( 4/2/1)
		○ 0~7
		○ chmod 750 .
		
	• tail
		○ 명령어 log볼 수 있음
		○ 실시간으로
		○ sudo tail -F /var/log/auth.log
		
