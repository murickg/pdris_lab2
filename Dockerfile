FROM ubuntu:latest
LABEL authors="muradgamzatov"
RUN apt-get update && apt-get install -y python3 python3-pip

EXPOSE 8081