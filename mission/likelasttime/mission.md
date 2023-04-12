###1. 컨테이너 기술이란 무엇입니까? (100자 이내로 요약)
컨테이너는 코드와 모든 의존성을 패키지화 한 소프트웨어의 표준 단위  
한 컴퓨팅 환경에서 다른 컴퓨팅 환경으로 빠르고 안정적으로 애플리케이션을 실행

###2. 도커란 무엇입니까? (100자 이내로 요약)
Docker는 애플리케이션을 개발, 배포, 실행하기 위한 오픈 플랫폼  
infrastructure에서 애플리케이션을 분리할 수 있게 해서 소프트웨어를 빠르게 배포 가능   
Docker는 애플리케이션을 관리하는 방법처럼 infrastructure를 관리 할 수 있음  
코드 작성과 실행 사이의 시간 지연을 줄일 수 있음

###3. 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?
* *도커 파일*  
    * Dockerfile을 통해 image를 자동으로 생성할 수 있음
    * 이미지를 구성하기 위해 command line에서 호출할 수 있는 모든 명령을 포함하는 text document

* *이미지*
  * Docker 컨테이너를 생성하는 read-only 템플릿  
  * 컨테이너의 파일시스템을 포함하고 있음
    * 애플리케이션을 실행하기 위해 필요한 모듯 것을 포함(dependencies, configurations, scripts, binaries, etc)
  * 다른 컨테이너의 설정도 포함(environment variables, a default command to run, and other metadata)

* *컨테이너*
  * 실행 가능한 이미지 인스턴스