# Background
利用 Flask + uwsgi + nginx + docker 实现 Pytorch 模型部署，采用 REST API 的形式进行接口调用

# Install
1. 生成镜像
```shell
docker-compose build
```

2. 启动容器
```shell
docker-compose up
```

# Usage
+ 通过编写简单 Python 脚本发送 POST 请求来测试项目的可用性
```python
import requests
resp = requests.post("http://127.0.0.1:8000/predict",files={"file":open("test.jpg","rb")})
print(resp.text)
```

+ 使用 apache2-utils 对该服务进行压力测试。其中 “-c” 表示并发数， “-n” 表示请求总数
```shell
ab -c 10 -n 100 -p test.jpg -T "application/x-www-formurlencoded" http://127.0.0.1:8000/predict
```
