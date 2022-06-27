## Neural Network Optimization
- 학습속도 향상
- Overfitting 방지

### Weight initialization
1. Xavier initialization
   1.  활성화 함수로 sigmoid, tanh 함수 사용 시 적용
   2.  다수의 딥러닝 라이브러리에 default로 적용돼 있음
   3.  표준편차가 √(1/n)  인 정규분포를 따르도록 가중치(ϴ) 초기화
2.  HE initialization
    1. 활섬화 함수로 ReLU 함수 사용 시 적용
    2. 표준편차가 √(2/n)   인 정규분포를 따르도록 가중치(ϴ) 초기화
     -  Ø N : 전 layer의 node 갯수  
    -  전 layer의 가중치(𝚹) 합이 너무 커지지 않도록 조절

### Weight regularization
1. Training data만 고려된 cost function을 기준으로 학습하기에
Overfitting 발생 가능성 높아짐
2. 모델이 복잡해질수록 모델 속 𝚹는 갯수가 많아지고 절대값이 커지는 경향
   1. 기존 cost function + Regularization 함수( 𝚹에 대한 함수) -> new cost function
3. L1 regulariztion (Lasso)
   1. 관련성이 없거나 매우 낮은 특성의 가중치𝚹를 0으로 유도
   2. Feature selection 효과 (Feature extraction)
4. L2 regulariztion (Ridge)
   1. 큰 값을 가진 가중치𝚹를 더욱 제약하는 효과
   2. Overfitting 감소에 더 효과적
5. Elastic net
Lasso, Ridge 모두 적용
   > Weight Decay(가중치 감퇴/감소)

* Regulariztion rate (𝜆 )
  * Hyper parameter
  * 𝜆 스칼라값
  * 정규화 함수의 상대적 중요도 지정
  * 정규화율을 높이면 overfitting 감소, 하지만 underfitting 가능
  * 𝚹의 수가 많은 신경망은 정규화율을 아주 작게 주기도 함

### Advanced gradient dcscent algorithms
1. (Full-Batch) Gradient Descent
   1. 학습이 오래걸림
   2. cost 그래프가 안정적
2. SGD (Stochastic Gradient Descent)
   1. Batch size = 1 마다 cost계산 -> Gradient descent 계산 -> weight 빠르게 업데이트
   2. 속도가 빠르다
   3. cost 그래프가 변동이 심해 안정적 감소중인지 예측 하기 어려움
3. Mini-Batch SGD
   1. Full batch 대비 batch 갯수 정함
   2. Batch size 만큼씩 cost 계산
   3. 의도에 따라 속도와 안정성 동시 관리 가능
   4. GPU 기반 효율적인 병렬 연산 가능
   5. Adam
   6. RAdam