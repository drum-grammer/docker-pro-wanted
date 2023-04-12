1. 명령어를 통해 이미지를 pull 받습니다.

```bash
$ docker pull ivykim/nestjs-prisma:latest
```

2. 명령어를 통해 도커 컨테이너를 실행합니다.

```bash
$ docker container run -dit --name nestjs-prisma ivykim/nestjs-prisma
```

3. 아래의 명령어를 통해 실행중인 컨테이너에서 명령어를 실행합니다.

```
$ docker exec -it nestjs-prisma /bin/sh
```

4. 서버를 실행합니다.

```
/usr/src/app $ npm run start:dev
```

```
> nestjs-prisma@0.0.1 start:dev
> nodemon --watch '**/**' --exec 'ts-node' ./src/main.ts

[nodemon] 2.0.22
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): **/**
[nodemon] watching extensions: ts,json
[nodemon] starting `ts-node ./src/main.ts`
[Nest] 54  - 04/10/2023, 1:57:50 PM     LOG [NestFactory] Starting Nest application...
[Nest] 54  - 04/10/2023, 1:57:50 PM     LOG [InstanceLoader] ConfigHostModule dependencies initialized +13ms
[Nest] 54  - 04/10/2023, 1:57:50 PM     LOG [InstanceLoader] AppModule dependencies initialized +0ms
[Nest] 54  - 04/10/2023, 1:57:50 PM     LOG [InstanceLoader] ConfigModule dependencies initialized +0ms
[Nest] 54  - 04/10/2023, 1:57:50 PM     LOG [RoutesResolver] AppController {/}: +13ms
[Nest] 54  - 04/10/2023, 1:57:50 PM     LOG [RouterExplorer] Mapped {/, GET} route +2ms
[Nest] 54  - 04/10/2023, 1:57:50 PM     LOG [NestApplication] Nest application successfully started +3ms
🚀 server is running on port 3095 🚀
```
