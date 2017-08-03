FROM python:3.6-alpine

RUN pip install kafka

ADD consumer.py producer.py /app/

WORKDIR /app/

CMD python $SERVICE
