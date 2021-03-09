# Background
PyTorch 模型的部署，常见有两种方式。第一种是利用 TorchScript 进行模型C++部署。 在工业上， Python 通常用来快速实现算法以及训练模型，而 C++则作为模型的生产工具。目前 PyTorch 能够将二者结合在一起，实现 PyTorch 模型部署的核心技术组件就是 TorchScript 和 Libtorch。在这种部署方式中，首先需要将 Pytorch 模型转换成TorchScript 模型，然后将该 Script 模型序列化成文件，最后在 C++ 中使用 Libtorch 库加载模型。
 
第二种部署方式是进行 web 部署，将 PyTorch 模型作为一种 Python 应用来提供服务，并采用 REST API 的形式进行接口调用。整体上采用 Docker + Flask + uwsgi + Nginx 的方式来部署 Pytorch 模型，并使用 Docker Compose 来对服务进行编排。

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
