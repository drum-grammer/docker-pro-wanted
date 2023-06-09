1. 컨테이너 기술이란 무엇입니까? (100자 이내로 요약)
   - 컨테이너 기술이란 애플리케이션과 필요한 모든 파일을 하나의 런타임 환경으로 묶는 데 사용하는 기술입니다. 
     단일 구성 단위로서 컨테이너는 모든 컨텍스트의 모든 운영 체제에서 쉽게 이동 및 실행할 수 있습니다.
2. 도커란 무엇입니까? (100자 이내로 요약)
   - Docker는 컨테이너화를 지원하는 중요한 소프트웨어 플랫폼입니다. 
     Docker에서 개발자는 컨테이너에 애플리케이션을 설계 및 구축하고, 애플리케이션을 테스트하고, 다른 시스템 및 환경으로 전달합니다.
3. 도커 파일, 도커 이미지, 도커 컨테이너의 개념은 무엇이고, 서로 어떤 관계입니까?
   - 도커파일
     도커파일은 "도커 이미지를 빌드하는 방법을 정의하는 스크립트"입니다.
     Docker에서는 환경 정보를 저장하는 파일을 도커파일이라고 합니다. 
     도커파일에는 컨테이너의 구동에 필요한 정보가 작성되어 있습니다.
   - 도커이미지
     도커 이미지는 "소스 코드, 라이브러리, 종속성, 도구 및 응용 프로그램을 실행하는데 필요한 기타 파일을 포함하는 불변(변경 불가) 파일"입니다.
     이미지는 읽기 전용이므로 스냅샷이라고도 하며, 특정 시점의 애플리케이션과 가상 환경을 나타냅니다.
     이러한 일관성은 도커의 큰 특징 중 하나로 개발자가 안정적이고 균일한 조건에서 소프트웨어를 테스트하고 실험할 수 있도록 합니다.
   - 도커컨테이너
     사용자가 기본 시스템에서 애플리케이션을 "분리할 수 있는 가상화된 런타임 환경"으로
     이러한 컨테이너는 응용프로그램을 빠르고 쉽게 시작할 수 있는 portable units 입니다.
     중요 기능은 컨테이너 내부에서 실행되는 컴퓨팅 환경의 표준화입니다.
     응용 프로그램이 동일한 환경에서 작동하도록 할 뿐 아니라 다른 사람과의 공유도 단순화합니다.
   - 이들의 관계 : 도커파일을 빌드해서 이미지를 생성 ->  도커이미지는 도커컨테이너를 생성하기 위한 템플릿 ->  도커컨테이너는 도커이미지가 실제 메모리에 로딩된 인스턴스입니다.



