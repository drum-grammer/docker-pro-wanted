# 실제 실무에서 사용하던 Dockerfile 예제
FROM golang:latest

RUN mkdir /appname
WORKDIR /appname
ADD bin/appname bin/appname
ADD conf conf
ADD public public
ARG BUILD_PORT
ENV PORT $BUILD_PORT
EXPOSE $BUILD_PORT
ENTRYPOINT ["bin/appname"]