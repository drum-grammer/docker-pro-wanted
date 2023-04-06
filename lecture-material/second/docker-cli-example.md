# command

```bash
docker network create wordpress_net
```

```bash
docker \
run \
    --name "db" \
    -v "$(pwd)/db_data:/var/lib/mysql" \
    -e "MYSQL_ROOT_PASSWORD=root_pass" \
    -e "MYSQL_DATABASE=wordpress" \
    -e "MYSQL_USER=docker_pro" \
    -e "MYSQL_PASSWORD=docker_pro_pass" \
    --network wordpress_net \
mysql:latest
```

```bash
docker \
    run \
    --name app \
    -v "$(pwd)/app_data:/var/www/html" \
    -e "WORDPRESS_DB_HOST=db" \
    -e "WORDPRESS_DB_NAME=wordpress" \
    -e "WORDPRESS_DB_USER=docker_pro" \
    -e "WORDPRESS_DB_PASSWORD=docker_pro_pass" \
    -e "WORDPRESS_DEBUG=1" \
    -p 8000:80 \
    --network wordpress_net \
wordpress:latest
```
