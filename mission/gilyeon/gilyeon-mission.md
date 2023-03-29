## I. 사전 미션
**1. 컨테이너 기술이란 무엇입니까?**
- 애플리케이션과 필요한 모든 자원을 하나의 런타임 환경으로 묶는 데 사용한다
하나의 OS 위에 여러 컨테이너가 구축될 수 있어, 애플리케이션간의 OS 자원을 공유할 수 있다.

**2. 도커란 무엇입니까?**
- Docker를 사용해 컨테이너를 구축하여 배포할 수 있고 이를 사용하면 인프라를 통일하게 사용 할 수 있으며,
여러 프로세스와 애플리케이션을 개별적으로 실행 가능하다.

**3. 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?**
- Dockerfile
  - 애플리케이션이 동작하는 환경을 구성하기 위해 패키지 설치, 환경변수 등록, 명령어 실행 등을 해야하는데 이를 한 번에 실행 할 수있게끔 Dockerfile을 사용한다.
즉 하나의 컨테이너를 만들기위해 설치해야하는 패키지, 소스코드, 명령어, 환경 변수 설정 등을 기록한 파일이다.

- Docker image
  - Dockerfile을 빌드하면 자동으로 Docker image가 생성된다.
이 Docker image는 Docker Hub에 올려서 공유가 가능하며, 반대로 Docker Hub에 올려진 image를 가져와서 사용가능하다.

- Docker container
  - Docker Container는 Docker image를 RUN하면 생성된다. 
Docker image는 Dockerfile에 작성된 명령어를 사용해 build된 하나의 정적파일이다. 
이를 포트 번호를 명시하여 RUN하면 Dokerfile에 작성된 환경대로 Container가 생성된다.

**4. [실전 미션] 도커 설치하기 (참조: [도커 공식 설치 페이지](https://docs.docker.com/engine/install/))**
- 아래 `도커 설치부터 실행 튜토리얼`을 참조하여 도커를 설치하고, 도커 컨테이너를 실행한 화면을 캡쳐해서 Pull Request에 올리세요.
  <img width="962" alt="스크린샷 2023-03-29 오전 10 28 28" src="https://user-images.githubusercontent.com/52391627/228403162-6210f60b-5dae-45b0-9017-eff4d94c3c84.png">



## II. 도커 설치부터 실행 튜토리얼
### 도커 설치
#### 1. 도커 공식 웹사이트에서 "[Get Started](https://www.docker.com/get-started)"를 클릭합니다.
#### 2. OS에 맞는 설치 파일을 다운로드 받습니다.
- MacOS의 경우 "Download for Mac"을 클릭합니다.
- Window 일 경우 "Download for Windows"를 클릭합니다.
- 다운로드한 설치 파일을 실행합니다.

### 도커 컨테이너 실행 시키기
#### 1. `나의 사전 미션 폴더`를 만들고 해당 폴더로 이동합니다.
```shell
cd path/to/docker-pro-wanted/mission
mkdir my-name
cd my-name
```

#### 2. "Hello, World!"를 출력하는 도커 파일을 만듭니다.
```shell
vim Dockerfile
```
`i`를 눌러 편집모드로 전환 후 아래 내용을 작성합니다:
```Dockerfile
FROM alpine:latest
CMD ["echo", "Hello, World"]
```
`ESC`를 눌러 명령모드로 전환 후, `:wq` 입력, `enter`키를 눌러 `Dockerfile`을 생성합니다.

#### 3. 도커 파일로 도커 이미지를 빌드합니다.
```shell
docker build -t hello-world .
```
(위 명령어의 의미는 "현재 디렉토리에서 `Dockerfile`을 읽어 도커 이미지를 만들고, 해당 이미지에 `hello-world`라는 `tag` 를 붙혀라" 입니다.)

#### 4. 빌드한 도커 이미지를 실행합니다.
```shell
docker run hello-world
```
이 명령어는 hello-world라는 이름의 도커 이미지를 실행시켜 "Hello, World!"를 출력합니다.
