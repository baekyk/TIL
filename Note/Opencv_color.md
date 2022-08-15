	• RGB
		○ grayscale 
			§ Y = 0.299R + 0.587G + 0.114B
			§ Green 성분이 가장 많이 들어감
		○ 장점 : 데이터 저장용량 감소, 데이터 처리 속도 향상
		○ 단점 : 색상 정보 손실
		
	• HSV
		○ Hue : 색상, 색의 종류
		○ Saturation : 채도 
		○ Value : 명도
		○ Intensity :
		○ Lightness
		○ HSV 값 범위
			§ cv2.CV_8U 경우
			§ 0<= H <= 179
			§ 0<= S <= 255
			§ 0<= V <= 255

	• YCrCb
		○ PAL, NTSC, SECAM 등 컬러 비디오 표준에 사용되는 색 공간
		○ 밝기, 색상정보 분리하여 부호화(흑백 TV호환)
		○ Y : 밝기 정보(luma)
		○ Cr, Cb : 색차(chroma)
		○ YCrCb 값 범위
			§ cv2.CV_8U 경우
			§ 0<= Y <= 255
			§ 0<= Cr <= 255
			§ 0<= Cb <= 255
		
