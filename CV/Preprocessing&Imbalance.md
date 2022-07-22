#### Preprocessing
- Resize
	- 각각 다른 사진 크기들
- Color
	- RGB, Gray, HN 등등
- Normalization
	- Scaling
	- 분포 수정


#### Class imbalance
  - Oversampling
    - 양은 늘수 있지만 다양성은 늘어나지 않을 수 있음
  - Augmentation
    - Augmentation 을 적용하면 다양성 늘어남
    - Epoch 양도 같이 늘려줌
    - Augmentations 은 특정 feature만 적용하지 않고 모든 데이터에 적용
      - 특정 데이터에만 적용 시 그 적용된 augmentation에 대해 잘못된 예측 가능
      -  다양성을 늘려주기 위해서 사용
    - Focal loss
      - 적은 비율의 데이터에 대한 loss값을 크게하여 학습에 대한 가중치 적용
    - 적은 비율의 데이터에 focus
