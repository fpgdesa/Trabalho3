FROM openwhisk/python3action:latest

RUN apk add --update py-pip
RUN apk add python3 python3-dev cmake make g++


RUN pip install scikit-build
RUN pip install ninja
RUN pip install numpy
RUN pip install --upgrade pip setuptools wheel
RUN pip install opencv-python


