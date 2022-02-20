FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY latency-test.py latency-test.py

ENTRYPOINT ["python", "latency-test.py"]
