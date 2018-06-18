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
  
