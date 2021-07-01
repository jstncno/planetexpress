FROM jenkins/jenkins:lts-alpine

USER root
RUN addgroup -g 998 docker
RUN addgroup jenkins docker

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install docker six

RUN apk add --update rsync

COPY scripts/ /opt/scripts/


USER jenkins
