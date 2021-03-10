# 背景
PyTorch 模型的部署，常见有两种方式。第一种是利用 TorchScript 进行模型C++部署。 在工业上， Python 通常用来快速实现算法以及训练模型，而 C++则作为模型的生产工具。目前 PyTorch 能够将二者结合在一起，实现 PyTorch 模型部署的核心技术组件就是 TorchScript 和 Libtorch。在这种部署方式中，首先需要将 Pytorch 模型转换成TorchScript 模型，然后将该 Script 模型序列化成文件，最后在 C++ 中使用 Libtorch 库加载模型。
 
第二种部署方式是进行 web 部署，将 PyTorch 模型作为一种 Python 应用来提供服务，并采用 REST API 的形式进行接口调用。整体上可采用 flask + uwsgi + nginx 的方式来部署 Pytorch 模型，并使用 docker 对其进行包装，使用 docker compose 来对服务进行编排，达到开箱即用的效果。

# 功能
该项目部署的 Pytorch 模型是用来进行猫狗识别的简单 CNN 网络，由客户端将图片发送至服务器端，服务器端在作出预测后将预测结果返回给客户。具体过程如下，对于客户端发送到主机 8000 端口的 HTTP 请求，使用 Nginx 容器将主机的 8000 端口映射到容器内的 80 端口；然后 Nginx 容器对请求进行负载均衡，发送到接口为 8080、 8081、 8082 等多个不同的 Flask 容器中； Flask 容器先通过 uwsgi 对请求进行处理，然后将请求的内容输入 Pytorch 模型中得到预测结果，并将结果返回到客户端。另外，可在 model.py 文件中更换需要的网络模型，使用新的网络模型参数 model.pth，或在 utils.py 文件中修改图片预处理方式，网络加载方式等。

![flame](https://github.com/FlowerForAlgernon/pytorch_web_deployment/blob/main/pic/flame.png)

# 安装
Docker 版本为 20.10.1

1. 在项目根目录下使用以下命令构建项目镜像
```shell
docker-compose build
```

2. 在项目根目录下使用以下命令启动项目容器
```shell
docker-compose up
```

# 测试
+ 在客户端通过编写简单 Python 脚本发送 POST 请求，将图片 test.jpg 发送到服务器端，检查返回值以测试项目的可用性
```python
import requests
resp = requests.post("http://127.0.0.1:8000/predict",files={"file":open("test.jpg","rb")})
print(resp.text)
```

+ 在客户端使用 apache2-utils 对该服务进行压力测试。其中 “-c” 表示并发数， “-n” 表示请求总数
```shell
ab -c 10 -n 100 -p test.jpg -T "application/x-www-formurlencoded" http://127.0.0.1:8000/predict
```
