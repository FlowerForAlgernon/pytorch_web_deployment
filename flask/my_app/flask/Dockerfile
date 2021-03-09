#FROM python:3.6
FROM pytorch/pytorch

WORKDIR /app
ADD . /app

RUN apt-get clean\
         && apt-get update   --fix-missing\
         && apt-get install libxml2  --assume-yes\
         && apt-get install gcc-4.8  --assume-yes\
         && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 100

RUN pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple