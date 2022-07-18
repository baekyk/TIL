#### Classification
   * Location
   * Classification


#### Detection
   * Location
   * Classification
   * Objection
   * 예시
     * YOLO


#### Tracking
   * Location
   * Classification
   * Objection
   * Object ID
    
   * 예시
     * DeepSORT  
        - SORT : single online real-time tracking  
           - Kalman filter
           - Hungarian algorithm
       - Feature extract
            □ Occlusion 감소
            □ Id switching 방지


#### Segmentation
   - Semantic segmentation
     - 모든 픽셀에 대해 class 예측
     -  No objects
   - Instace segmentation
     - Multiple object에 대해
     - Location 후 그 위치에서 어떤 픽셀이 어떤 class에 속하는지 예측
   - Dataset for image segmentation
     - Coco dataset
       - Polygon 형태로 labeling 후 각 꼭지점의 좌표 포인트들을 json으로 저장
	
