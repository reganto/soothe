## Instruction

- install **tornado**

```bash
pip install tornado
```

- create docker image from Dockerfile

```bash
docker build -t tornado-image .
```

- install **supervisor**

```bash
pip install supervisor
```

- run **supervisord**

```bash
supervisord -c supervisor/init.conf
```

- run **supervisorctl** or open http://localhost:9001 in your browser to manage processes.

> Best practice: don't use **inet_http_server** in production unless you provide security for it.

- set nginx settings for load balancing

`vi /etc/nginx/conf.d/default.conf`

```bash
upstream backend {
    server localhost:8000 weight=2;
    server localhost:8001 weight=1;
    server localhost:8002 weight=1;
    server localhost:8003 backup;
}
server {
    location / {
        proxy_pass http://backend;
    }
}
```

- test nginx configs

`nginx -t`

- reload nginx configs

`nginx -s reload`

- open browser and go to `localhost`

