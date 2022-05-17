## Instruction

- install **tornado**

```bash
pip install tornado
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

> Best practice: don't use **inet_http_server** in production unless you provide security for that.