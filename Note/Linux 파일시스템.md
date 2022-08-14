	• find
		○ 검색
		○ find 파일명
		○ find . -name "*.txt"
		○ find . -name "hello*" -type f : 파일 찾는것
			§ type d : 디렉토리
		○ find . -size +10M   : 용량 10M 이상 파일
		○ find -newerct '15 May 2022' -ls
			§ newerct : 최근 생성
			§ newermt : 최근 변경
	• stat
		○ 속성
		○ access : 접근 시간
		○ modify : 변경 시간
		○ change : 수정 시간 ( inode 관점)
		○ ls -l : 기본 (mtime)
		○ ls -l -u : atime
		○ ls -l -c : ctime
	• sort
		○ ls -l | sort
		○ ls -l | sort -k 2 : 두번째 컬럼 기준
		○ ls  -l | sort -k 2n  : 두번쨰 숫자 기준
		○ ls -l | sort -r : 내림차순
		○ ls -l | sort -k 2n -k5 : 두번째 & 다섯번째 기준
	• awk
		○ 패턴 검색 및 텍스트 프로세싱
		○ ls -l | awk '{print $1}' : 첫번째 컬럼만 출력
		○ ls -l | awk '{sum += $5} END {print sum}' : 5번 컬럼 모두 더해서 출력
		○ awk '$5 >= 10000 {print}' : 10000보다 큰것 출력
		○ awk -F':' '{print $1}' : 콜론을 구분자로 잘라서 첫번째 컬럼 출력
	• sed
		○ 내용 검색/편집
		○ sed 's/패턴/변환/g'
		○ sed 's/book/books/g' : book 을 books 로 변경
		○ sed 's/.$/!/g' : 마지막을 !로 변경
		○ sed 's/[a-z]/\U&/g' : 소문자 -> 대문자
	• uniq
		○ 중복 제거
	• wc
		○ 라인수/단어수/문자수 출력
	• du
		○ disk usage
		○ 파일 용량 출력
		○ -k, -m 
		○ -h : 사용자 편의 용량
		○ -s : 합계
	• tar
		○ 파일 묶음
		○ tar cvf myzip.tar dir1  : 묶기
		○ tar xvf myzip.tar  : 풀기
	• gzip, bzip2, xz
		○ 압축
		○ gzip filename
		○ gzip -d filename
		
		
