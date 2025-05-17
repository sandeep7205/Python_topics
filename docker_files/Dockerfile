FROM ubuntu:latest

LABEL maintainer="Sandeep Kumar Mishra"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/* 

WORKDIR /app

CMD ["bash"]
 