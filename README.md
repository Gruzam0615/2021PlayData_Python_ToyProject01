# 2021PlayData_Python_ToyProject01
2021 플레이데이터 - 데이터엔지니어링6기 - 파이썬 토이프로젝트

---------------------
####  미니 프로젝트 주제, 기능 선정 
#### 21.09.16
#### 팀명 : 3팀 
#### 팀원 : 김기영 김현진 박민재 한다예 
#### 팀장 : 김기영 
#### 주제 : 생필품 가격정보

---------------------

# 사용 가능한 오퍼레이션 
    - 상품정보 조회
    - 판매점 정보 조회
    - 생필품 가격정보 조회
    - 생필품 가격 정보 기준 데이터 조회
 
# 상품정보 조회

- 요청 데이터 : 상품 아이디 
- 응답 데이터 : 상품명, 상품 설명, 상품 용량

# 판매점 정보 조회 
- 요청 데이터 : 업체 아이디
- 응답 데이터 : 업체 명, 업태 코드, 지역_상세_코드, 전화번호, 지번_기본_주소_명, 지번_상세_주소_명,
            X_지도_좌표, Y_지도_좌표       

# 생필품 가격 정보 조회
- 요청 데이터 : 상품 조사일, 업체 아이디, 상품 아이디 
- 응답 데이터 : 상품 조사일, 업체 아이디, 상품 아이디, 상품 가격, 원플러스원 여부, 
            상품 할인 여부, 상품 할인 시작일, 상품 할인 종료일, 입력 일시
 
# 기능 

- 상품 판매점 검색 -> 위치 검색(지도)
- 상품 원플러스원 판매점 검색
- 상품 할인 판매점 검색
- 상품 고유 정보 검색
- 상품 최근 가격 -> 여러 상품 가격 비교   
- 상품 가격 편동 정보 -> 그래프 
- 지역별 업체 수
- 판매점 별 많이 다루는 품목
- 상품 별 자주 할인 하는 기간

---------------------

#### 21.09.17

## 기능 구현 계획
1. 코드로 되어있는 것들 값 가져와서 출력
2. 상품 분류별 정보(통계, 가격 변동률 등)
3. 판매점 이름으로 정보 검색
4. 상품 가격 변동 그래프
5. 상품 가격 최고, 최소, 평균 출력
6. 상품 원플러스원 판매점 검색
7. 상품 할인 판매점 검색
8. 지역별 업체수
9. 목록에서 검색 기능
10. 할인 빈도 (할인 Y 개수로)
11. 원플러스원 빈도(1+1 Y 개수로)
12. 업태별 최저가 목록

- 김기영: 1 2 12
- 김현진: 8 10 11
- 박민재: 4 5 9
- 한다예: 3 6 7

#### 21.09.27
기존의 10. 11. 12 항목은 제외
완료된 기능
1. 상품목록조회
2. 상품이름으로 검색
3. 판매점 목록조회
4. 판매점이름으로 검색
5. 판매점 주소로 검색
6. 지역별 판매점 업체 수
7. 상품 이름과 날짜로 가격 검색
8. 상품 이름과 날짜로 할인 판매점 및 가격 검색
9. 상품 이름과 날짜로 해당 날짜의 평균가, 최고가, 최저가 검색
10. 시작일과 종료일, 평균, 최저, 최고 가격 변동률
11. 기간내 가격 변동 그래프

#### 21.09.28
#### 사용 가능한 오퍼레이션 
    - 1. 상품정보 조회
    - 2. 판매점 정보 조회
    - 3. 생필품 가격정보 조회
    - 4. 생필품 가격 정보 기준 데이터 조회

#### 4일차 진행
#### 오전  
- 한다예 : 구글 스타일 센터 로고 + 상품 이름으로 검색창, 검색한 상품의 가격 변동 그래프 나올 수 있는지 
- 박민재 : Home 버튼 왼쪽으로, 조각페이지, 센터로 정렬 
- 김현진 : 테이블 정렬, 상세 주소 합치기  
- 김기영 : 부트스트랩 기본 구조 정립

- 기능 통합, 정리 완료, 디자인 완성 단계 
- 추가로 해보고 싶은 기능, 디자인 각자 진행 예정 
- 에러 처리 진행 예정

# 참고 
https://matplotlib.org/stable/index.html
https://ehclub.net/677
https://zephyrus1111.tistory.com/36
https://truman.tistory.com/103
https://wikidocs.net/141547
https://www.price.go.kr/tprice/portal/main/main.do
