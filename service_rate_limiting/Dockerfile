FROM python:3.8

WORKDIR /rate_limiting_service

COPY ./service/requirements.txt /rate_limiting_service/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
  && apt-get install -yqq --no-install-recommends apt-utils\
    netcat \
  && apt-get -q clean
RUN pip install psycopg2
RUN pip install -r /rate_limiting_service/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /rate_limiting_service/
RUN chmod +x start_postgres.sh
EXPOSE 5000
CMD ["./start_postgres.sh"]