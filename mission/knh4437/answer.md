## II. 사전 미션
---

### 컨테이너 기술이란 무엇입니까? (100자 이내로 요약)
&nbsp;애플리케이션을 작동하기 위해 필요한 라이브러리나 어플리케이션 등을 하나로 모아, 마치 별도의 서버인 것처럼 사용할 수 있게 만들어 놓은 것을 일컫는다.
<br>

### 도커란 무엇입니까? (100자 이내로 요약)
&nbsp; 필요한 모든 종석성 및 라이브러리를 포함하여 애플리케이션을 위한 격리된 환경을 생성하고, 다양한 컴퓨팅 환경에서 일관되고 안정적인 성능을 보장해주는 플랫폼

### 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?
#### Docker Image
    - 서비스 운영에 필요한 서버 프로그램, 소스 코드 및 라이브러리, 컴파일러된 실행 파일을 묶은 형태
    - Docker file을 빌드하여 생성된다.
    - 이미지가 빌드되면 DockerHub와 같은 레지스트리에 저장하고 다른 사람과 공유가 가능하다.

#### Docker file
    - Docker Image를 빌드하는데 필요한 단계를 정의하는 스크립트

#### Docker Container
    - 단일 애플리케이션 또는 프로세르르 실행는 격리된 환경
    - Docker Image에서 생성되며, Application을 실행하는데 필요한 모든 종속성 및 구성을 포함한다.
    - 임시적 환경으로 다른 컨테이너에 영향을 주지 않고, 쉽게 생성, 파괴 및 교체가 가능하다.