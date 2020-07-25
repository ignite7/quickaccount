FROM selenium/standalone-chrome

SHELL ["/bin/bash", "-c"]

USER root

RUN apt-get update && apt-get install \
    python3.8 python3-pip -y

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt

CMD tail -f /dev/null