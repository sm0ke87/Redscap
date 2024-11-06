FROM debian:trixie-slim

ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get -y install python3 && ln -sf python3 /usr/bin/python
RUN apt-get -y install wget openscap-scanner openscap-utils openssh-client
WORKDIR /opt
ADD /redos_orig.xml /opt/redos_orig.xml
ADD /main.py /opt/main.py
ADD /id_rsa /opt/id_rsa

SHELL ["/bin/bash", "-c"]
ENV SSH_ADDITIONAL_OPTIONS='-i /opt/id_rsa -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null'

ENTRYPOINT ["python", "main.py", "-l"]
