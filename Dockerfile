FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV PROVIDER=apollo
ENV APOLLO=false

RUN apt-get update && apt-get install --install-recommends -y apt-utils cron python3.8 python3.8-dev python3-pip python3-wheel && \
 apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

WORKDIR /m3u2strm

RUN bash -c 'mkdir -p ./m3u'

COPY *.py ./

VOLUME /movies /tv /events /logs

COPY initialize_cron.sh /root/

RUN chmod +x /root/initialize_cron.sh

RUN crontab

RUN (crontab -l) | crontab
