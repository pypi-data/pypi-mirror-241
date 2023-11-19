# 使用官方Python运行环境作为基础镜像
FROM python:3.11-slim

LABEL maintainer="ming.Li"
LABEL version="0.4"

RUN mkdir -p /root/.pip && \
    echo '[global]\nindex-url = https://mirrors.aliyun.com/pypi/simple/\n[install]\ntrusted-host = mirrors.aliyun.com' > /root/.pip/pip.conf

# 设置工作目录为/app
WORKDIR /app

# 将当前目录下的文件复制到容器中的/app
COPY pyproject.toml /app/

# 安装项目依赖项
RUN pip install .

# 将当前目录下的文件复制到容器中的/app
COPY . /app

# 通知Docker服务将在9000端口上运行
EXPOSE 9000

# 当容器启动时运行Uvicorn服务器
ENTRYPOINT ["python3","-m","markji_wordcard_assistant"]
