FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip libgl1 libglib2.0-0 ffmpeg && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install zephyr-rtsp

COPY . /workspace
WORKDIR /workspace
