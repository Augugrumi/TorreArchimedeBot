FROM python:3.6-slim

MAINTAINER Davide Polonio <poloniodavide@gmail.com>
LABEL A simple bot to see Torre Archimede room scheduling

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "-m", "./torrearchimedebot/" ]
