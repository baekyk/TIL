## Dropout
1. Training 진행할때 매 Batch마다 Layer 단위로 일정 비율만큼의 Neuron을 꺼뜨리는 방식
2. 동일 데이터에 매번 다른 모델 학습 시키는 방법으로 Model ensmble 효과를 얻을 수 있음
3. 보통 마지막 1~2개 hidden layer에 적용시킴
    
## Batch Normalization
1. Input data에 standardization과 같은 normalization을 적용하면 전반적으로 model 성능이 높아짐
2. Column 들의 scale에 model이 너무 민감해지는 것을 막아줌
3. Normalization 시 train, test 분리 후 train에 대해서만 fit 한 뒤 train, test 데이터에 적용
4. 각 layer의 node의 연산 순서
   1. 선형 결합 
   2. batch_normalization
   3. scaling & shifting(non-linearity) - 𝜆와 𝛽 는 parameter(𝜃)
   4. activation function
5. 장점
   1. 학습속도, 결과 개선
   2. 가중치 초기값에 크게 의존하지 않음
   3. Overfitting 억제
   4. 핵심은 학습 속도 향상
   5. overfitting을 억제하기 위한 부수적인 방법

## Over-parameterized
1. Deep Double Descent
2. 신경망의 depth와 width를 계속 늘려 복잡도를 늘리면 overfitting 단계를 지나 더 error가 적어질 수 있음
		
		
