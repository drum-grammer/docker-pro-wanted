1. 컨테이너 기술이란 무엇입니까? (100자 이내로 요약)
    - 리눅스에서 유래된 가상화 기술의 일종으로, 애플리케이션을 격리된 환경에서 실행하고 관리하는 기술
    - 애플리케이션을 환경에 구애받지 않고 실행할 수 있음

2. 도커란 무엇입니까? (100자 이내로 요약)
   - Docker는 컨테이너화를 지원하는 중요한 소프트웨어 플랫폼입니다. 
     Docker에서 개발자는 컨테이너에 애플리케이션을 설계 및 구축하고, 애플리케이션을 테스트하고, 다른 시스템 및 환경으로 전달합니다.

3. 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?
    - 도커 파일: docker 에서 이미지를 생성하기 위한 용도로 작성하는 파일이다. 만들 이미지에 대한 정보를 기술해 둔 템플릿(template) 이라고 보면 된다.
    - 도커 이미지: 컨테이너를 생성할 때 필요한 요소이며, 도커 파일을 build하여 생성.
      - [저장소 이름]/[이미지 이름]:[태그] 형태로 구성.
    - 도커 컨테이너: 도커 이미지를 통해 생성되며, 해당 이미지의 목적에 맞는 파일이 들어 있는 파일시스템과 격리된 시스템 자원 및 네트워크를 사용할 수 있는 독립된 공간.
    - 이들의 관계 : 도커 파일을 build해서 이미지를 생성 ->  도커 이미지는 도커 컨테이너를 생성하기 위한 템플릿 ->  도커 컨테이너는 도커 이미지가 실제 메모리에 로딩된 인스턴스입니다.

4. [실전 미션] 도커 설치하기
    - `./capture-headgen.png`로 업로드함.
