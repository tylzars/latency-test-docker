FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY latency-test.py latency-test.py

ENV DESTINATIONS = "google.com"
ENV DATABASE-IP = "192.168.1.1"


ENTRYPOINT ["python", "latency-test.py"]
