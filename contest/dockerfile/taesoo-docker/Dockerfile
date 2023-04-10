# Build Stage
# builder 라는 이미지 생성
FROM openjdk:11 AS builder

# 생성한 이미지의 workDir 을 /app으로 지정
WORKDIR /app

# 왼쪽에 써있는것들을 이미지 내부의 오른쪽에 써있는 dir 로 복사
COPY gradle gradle
COPY gradlew .
COPY settings.gradle .
COPY build.gradle .
COPY src src

# ./gradlew 의 권한변경 후 클린과 빌드 실행
RUN chmod +x ./gradlew
RUN ./gradlew cleanQuerydslSourcesDir
RUN ./gradlew build -x test --no-daemon
# RUN ./gradlew clean build -x test --no-daemon

# Runtime Stage
# jre 이미지 생성
FROM openjdk:11-jre-slim

## 환경변수 설정 및 workDir 을 환경변수로 설정한 경로로 지정
ENV APP_HOME=/usr/app/
WORKDIR $APP_HOME

## 처음에 생성했던 이미지파일내부에서 빌드했던 파일을 지금 생성한 이미지 내부에 복사
COPY --from=builder /app/build/libs/*SNAPSHOT.jar .

# 포트설정
EXPOSE 8080

# 이미지 실행시 실행할 명령어 설정
CMD ["java", "-jar", "jpashop-0.0.1-SNAPSHOT.jar", "-Dspring.profiles.active=docker"]
