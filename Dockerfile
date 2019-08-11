FROM python:3
ENV PYTHONUNBUFFERD 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update && apt-get install -y \
 libgeos-dev \
 libproj-dev \
 proj-data \
 proj-bin \
 libgdal-dev \
 python-gdal \
 gdal-bin \
 postgis
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
COPY ./wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
