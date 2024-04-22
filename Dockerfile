FROM ubuntu:20.04

ARG PUID=1024
ARG PGID=100
ARG UID=1024
ARG GID=100
ARG UNAME=admin
ARG GROUP=users
ARG DEBIAN_FRONTEND=noninteractive
ENV APOLLO=false
ENV SINGLELIST=true
ENV MOVIES=false
ENV TVSHOWS=false
ENV EVENTS=false
ENV CRONMINUTE=3
ENV CRONHOUR=00
ENV TVCRONMINUTE=3
ENV TVCRONHOUR=00
ENV MOVIECRONMINUTE=3
ENV MOVIECRONHOUR=00
ENV EVENTCRONMINUTE=3
ENV EVENTCRONHOUR=00
ENV SINGLELISTURL=''
ENV TVSHOWURL=''
ENV MOVIEURL=''
ENV EVENTURL=''

RUN getent group ${GROUP} || groupadd -g ${GID} ${GROUP}

RUN useradd ${UNAME} -u ${UID} -g ${GID} -m -s /bin/bash || echo "user already exists"

RUN apt-get update && apt-get install --install-recommends -y apt-utils cron python3.8 python3.8-dev python3-pip python3-wheel vi && \
 apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

RUN mkdir /m3u2strm && chown ${uid}:${gid} /m3u2strm

USER ${uid}

WORKDIR /m3u2strm

RUN bash -c 'mkdir -p ./m3u'

COPY *.py ./

VOLUME /movies /tv /events /logs

COPY initialize_cron.sh /m3u2strm/

RUN chmod +x /m3u2strm/initialize_cron.sh

RUN crontab

RUN (crontab -l) | crontab
