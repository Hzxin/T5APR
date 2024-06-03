FROM ubuntu:22.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt install -y \
    nano git curl wget \
    python3-pip \
    build-essential libssl-dev libffi-dev python3-dev \
    python3-venv

WORKDIR /opt
RUN git clone --recurse-submodules https://github.com/Hzxin/T5APR.git
RUN chmod +x /opt/*
WORKDIR /opt/T5APR

# Set up env
RUN python3 -m venv .venv && \
    /bin/bash -c "source .venv/bin/activate && \
    python3 -m pip install -U pip setuptools && \
    pip install -r requirements.txt"


