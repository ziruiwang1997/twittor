FROM python:3.6-alpine

LABEL maintainer="Peng Xiao <xiaoquwl@gmail.com>"

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

#将工程代码复制到容器内，镜像固化
COPY . /twittor

WORKDIR /twittor


#在构建镜像的时候，通过requirements.txt内的配置 ，定制安装需要的第三方库
RUN pip install -r requirements.txt && pip install gunicorn&&chmod 755 run_server.sh

EXPOSE 8000

ENTRYPOINT [ "./run_server.sh" ]
