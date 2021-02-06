FROM python:alpine3.7
WORKDIR /app
COPY . /app
RUN set -xe \
    && apk update \
    && apk add --no-cache python3 py3-pip \
    && pip3 install --upgrade pip \
    && apk add --update musl-dev gcc libffi-dev \
    && apk add build-base \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && pip3 install -r ./requirements.txt 
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
