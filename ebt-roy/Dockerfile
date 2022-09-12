FROM python:3

WORKDIR /app

ADD requirements.txt .
ADD roy.py .

RUN pip install -r requirements.txt

ENTRYPOINT ["python","roy.py"]