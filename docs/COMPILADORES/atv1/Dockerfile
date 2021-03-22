FROM python:3.9-buster

COPY ./src/requirements.txt src/requirements.txt
RUN apt update -y
RUN apt libsdl2-dev libsdl2-image-dev gifsicle -y
RUN pip install --upgrade pip && pip install -r /src/requirements.txt

COPY . src
WORKDIR /src

ENTRYPOINT ["tail", "-f", "/dev/null"]