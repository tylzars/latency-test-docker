FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY latency-test.py latency-test.py

ENV DESTINATIONS "google.com"
ENV DATABASE-IP "192.168.1.1"
ENV DATABASE-NAME "latency"
ENV DEVICE-NAME "DEFAULT-DEVICE"
# Default InfluxDB Port
ENV DATABASE-PORT "8086"

ENTRYPOINT ["python", "latency-test.py"]
