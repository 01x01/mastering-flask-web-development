FROM python:3.6.5
# 配置工作目录
WORKDIR /app
# 拷贝当前目录文件到 app 文件夹
ADD . /app
# 安装依赖
RUN pip install -r requirements.txt
# 环境变量
ENV FLASK_APP=server.py
ENV FLASK_DEBUG=0
# 运行
