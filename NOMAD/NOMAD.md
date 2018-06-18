# NOMAD
  참조 링크: http://www.cs.utexas.edu/~inderjit/public_papers/nomad_ieee_computer_2016.pdf
  
## 연구 소개
 NOMAD 는 Non-Locking stOchastic Multimachine Framework for Asynchronous and Decentralized Machines 의 약자이다. 
 NOMAD 의 목표는 Big Data Optimization 을 하는데에 필요한 시간을 줄이고 더 좋은 solution 을 구하기 위한 알고리즘이다.

###### 연구원 소개
> Hsiang-Fu Yu, University of Texas at Austin  
Cho-Jui Hsieh, University of California, Davis  
Hyokun Yun, Amazon.com  
S.V.N. Vishwanathan, University of California, Santa Cruz  
Inderjit Dhillon, University of Texas at Austin  

---

## Data Optimization 
 Data Optimization 은 주어진 Dataset 에 알고리즘을 적용해서 분석을 하는 것 이다.
 
 Data Optimization 의 종류는 다양하기 때문에 한가지의 알고리즘으로 모든 Big Data Analysis 를 진행할 수 없다.  
 
 > Data Optimization 에는 명확한 값이 존재하는 데이터로 함축적인 값을 찾는 Matrix Completion 문제, 주어진 문서에서 연관되어 있는 단어를 분석하는 
 Topic Modeling 문제 등이 있다. 문제 별로 변수와 최종적으로 구하는 값의 종류 (확률 (%) 정확한 수 (#)) 이 다르다.
 
 NOMAD 알고리즘은 하나의 '틀' 이다. 다양한 Data Optimization 을 하기 위해서는 각 Data Optimization Problem 의 변수, 수학적인 공식 등 을 고려하고 NOMAD 라는 기본적인 틀을 
 커스터마이즈 해야한다.
 
> 현재 NOMAD 알고리즘은 Matrix Completion 과 Latent Dirichlet Completion, 두 종류의 Optimization Problem 에 적용해서 사용 할 수 있다.  Matrix 
Completion 은 주어진 값으로 함축적인 값을 추리 하는 문제다. Latent Dirichlet Completion 은 Topic Modeling 문제다. 

---

### 현재 데이터 분석 알고리즘
  현재 Data Optimization 을 위해서 사용하는 대표적인 알고리즘은 Stochastic Optimization 하고 Map-Reduce Algorithm 이다. 
  
![차트1](Python/NOMAD/ProsAndCons.png)
  
  >> Stochastic Optimization 하고 Map-Reduce Algorithm 의 장 단점을 보여주는 차트. NOMAD 알고리즘은 이 두 가지 알고리즘의  
  장점을 합치고, 단점을 없앤다.
  
## NOMAD 를 Matrix Completion 에 적용
  Matrix Completion 은 실존하는 데이터 값을 이용해 명확하지 않은 데이터값을 구하는 Data Optimization 문제다. 
  
  예)
  > Netflix 는 각종 드라마와 영화를 스트리밍하는 기업이다. Netflix 는 사용자가 기존에 봤던 영화, 그 영화에 대한 평판 등의 데이터를
  고려하고 다른 영화를 추천해준다. 하지만 사용자가 실제로 평판을 남기는 경우는 영화 10개당 3개 남짓한다. Netflix 는 사용자에게 효과적으로
  영화를 추천 해주기 위해서 사용자의 반응을 예상 해야된다. 사실 이 Prediction Algorithm 에는 엄청난 수의 요인이 들어간다. (장르, 주연배우, 
  감독, 영화를 본 시기 등) 하지만 기본적인 Raw Data (사용자, 영화, 평점) 으로만 평가 하기 위해서는 Matrix Completion 을 쓸수있다  
  Matrix 의 행을 사용자, 열을 영화라고 가정을한다. Matrix 의 인풋 데이터는 특정 사람이 특정 영화에 내린 평점이다. 예를 들면 
  철수의 모든 영화 데이터는 2번째 행에 나열되어있고 인셉션 이라는 영화의 평점이 3번째 열에 나열되어 있으면 철수가 인셉션에 대한 평점은 
  2번째행 3번째열에 저장되어 있다 (철수가 인셉션을보고 평가를 했을 시).  
  철수가 인셉션을 관람 하지 않았거나 관람 후 평점을 내리지 않았으면 2번째 행 3번째 열의 값은 비어있다. 이 비어있는 칸의 값을 예상 하는 것이
  Matrix Completion 의 기본 문제다. 
  
  Matrix Completion 의 가장 기본적인 공식은 유클리디언 벡터 공간을 통한 계산이다.  
  

  
  
  
