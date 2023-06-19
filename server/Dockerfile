FROM python:slim-buster
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential
COPY req.txt /server/req.txt
WORKDIR /server/
RUN pip3 install -r req.txt