## cli example

### 1. [Download an image from a registry](https://docs.docker.com/engine/reference/commandline/pull/)
- 사용법
```shell
 docker pull [OPTIONS] NAME[:TAG|@DIGEST]
```
- 예제
```shell
docker pull httpd
```

### 2. [List images](https://docs.docker.com/engine/reference/commandline/images/)
- 사용법
```shell
 docker images [OPTIONS] [REPOSITORY[:TAG]]
```
- 예제
```shell
 docker images
```

### 3. [Create and run a new container from an image](https://docs.docker.com/engine/reference/commandline/run/)
- 사용법
```shell
 docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```
- 예제
```shell
 docker run httpd
 docker run --name secondContainer httpd
 docker run -p 8888:80 -v ~/wanted/pre-mission/docker-pro-wanted/lecture-material:/usr/local/apache2/htdocs httpd

```

### 4. [Stop one or more running containers](https://docs.docker.com/engine/reference/commandline/stop/)
- 사용법
```shell
 docker stop [OPTIONS] CONTAINER [CONTAINER...]
```
- 예제
```shell
 docker stop 9b0f49de746c
 docker stop -a
```

### 5. [Fetch the logs of a container](https://docs.docker.com/engine/reference/commandline/logs/)
- 사용법
```shell
 docker logs [OPTIONS] CONTAINER
```
- 예제
```shell
docker logs second
docker logs second -f
```

### 6. [Remove one or more containers](https://docs.docker.com/engine/reference/commandline/rm/)
- 사용법
```shell
 docker rm [OPTIONS] CONTAINER [CONTAINER...]
```
- 예제
```shell
docker rm 6026ab9b44cc
docker rm second -f
```

### 7. [Remove one or more images](https://docs.docker.com/engine/reference/commandline/rmi/)
- 사용법
```shell
 docker rmi [OPTIONS] IMAGE [IMAGE...]
```
- 예제
```shell
docker rmi 6026ab9b44cc
```

## Dockerfile 활용
1. Dockerfile 예제
```Dockerfile
FROM httpd:latest
COPY  index.html /usr/local/apache2/htdocs/index.html
EXPOSE 80
```
2. 이미지 만들기
```shell
docker build -t my-httpd .
```
3. 도커파일로 생성된 이미지로 컨테이너 실행하기
```shell
docker run -d -p 8888:80 my-httpd
```
