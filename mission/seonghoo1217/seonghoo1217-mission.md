## 1. 컨테이너 기술이란 무엇입니까?
- 컨테이너 기술은 응용 프로그램을 실행하는 데 사용되는 가상화 기술로 독립적인 환경을 제공하고, 대표적인 기술로는
`Docker`가 존재합니다.

## 2. 도커란 무엇입니까?
- `Docker`란 컨테이너 기술을 이용하여, 응용프로그램을 만들고 배포하는 플랫폼이다.
- 요소들을 패키지화하여 컨테이너 단위로 관리하여 확장성이 좋다.

## 3. 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?
셋다 `Docker` 플랫폼을 구성하는 요소들이지만 각자 다른 역할을 수행합니다.

`Docker File(도커파일)`은 도커 이미지를 생성하기 위한 설정 파일입니다. 해당 설정에는 아래의 값들을 필요로합니다.
- 구성 패키지
- 응용 프로그램
- 환경 변수
- 포트

해당 정보들은 빌드 프로세스에서 사용되며 새로운 파일 시스템 레이어를 가진 독립적인 파일이 됩니다.

`Docker Image(도커 이미지)`는 도커 파일을 사용한 빌드 결과로 컨테이너를 실행하는데 있어, 필요한 모든 것이 포함된 패키지입니다.
즉, Docker 이미지는 응용 프로그램과 그 구성요소, 운영 체제, 라이브러리 종속성 등을 포함합니다. 또한 읽기 전용으로 생성됩니다.

`Docker Container(도커 컨테이너)`는 도커 이미지를 기반으로 생성된 실행 가능한 인스턴스입니다.
즉, 도커 컨테이너는 도커 이미지에서 생성된 파일 시스템 레이어 위에 실행 환경이 추가된 것입니다. 도커 컨테이너는 호스트 운영 체제와 격리되어 있으며, 자체 파일 시스템과 네트워크를 가지고 있습니다.
도커 컨테이너는 이미지에서 생성되며, 하나의 이미지에서 여러 개의 컨테이너를 생성할 수 있습니다.

따라서, 도커 파일은 도커 이미지를 만들기 위한 설정 파일이고, 도커 이미지는 응용 프로그램 및 실행 환경을 포함하는 패키지입니다.
도커 컨테이너는 도커 이미지에서 생성된 실행 가능한 인스턴스이며, 도커 이미지를 기반으로 작동합니다.
도커 파일을 사용하여 도커 이미지를 빌드하고, 해당 이미지를 사용하여 도커 컨테이너를 생성하여 응용 프로그램을 실행할 수 있습니다.