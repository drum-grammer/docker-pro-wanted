# 사전 미션

## 컨테이너 기술이란 무엇입니까?

- 기존의 하이퍼바이저 기반의 가상머신 기술은 하나의 가상머신에 게스트 OS를 포함한 환경을 구축해서 게스트 OS를 통해 가상화된 자원을 할당해 응용 프로그램을 개발하는 형태였습니다. 하지만 이 기술은 게스트 OS를 포함하기 때문에 하나의 가상 머신의 크기가 너무 크다는 단점이 있었습니다. 컨테이너 기술은 리눅스의 cgroup과 namespace를 사용해서 컨테이너와 컨테이너를 격리시키고 호스트 OS로부터 자원을 직접 할당받는 형태로서 호스트 OS와 커널을 공유해 접근이 더 쉽고 더 가벼운 장점을 가진 가상화 기술입니다.

## 도커란 무엇입니까?

- 도커는 컨테이너 가상화 기술을 사용하는 프로그램으로 클라이언트로는 도커 CLI를 서버로는 리눅스를 사용하는 도커 서버를 가지고 있습니다. 응용 프로그램과 해당 프로그램에 필요한 리소스들을 컨테이너화하여 사용자에게 컨테이너를 통한 다른 기술들을 사용해 관리를 용이하게 할 수 있게 해주며 여기서 관리의 의미는 지속적인 배포, 테스트 자동화 등을 의미합니다.

## 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?

- 도커 파일은 도커를 사용해 도커 이미지를 생성하는 데에 필요한 명세를 가진 파일입니다. 필요한 명세로는 베이스 이미지의 명시와 이미지가 컨테이너로서 실행되기 전에 필요한 종속성 등의 설치를 위해 필요한 명령어, 컨테이너로서 실행될 때 필요한 실행에 대한 명령어 등이 있습니다. 도커 이미지는 도커 파일을 통해 생성된 응용 프로그램을 위해 필요한 모든 리소스의 스냅샷이라고 할 수 있습니다. 이러한 도커 이미지는 실행되는 런타임에 도커 컨테이너가 되며 도커 컨테이너는 도커 이미지의 인스턴스라고 할 수 있습니다.