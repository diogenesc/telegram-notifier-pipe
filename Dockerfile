FROM python:3.8-slim

COPY requirements.txt /
WORKDIR /
RUN pip install --no-cache-dir -r requirements.txt

COPY . /

ENTRYPOINT ["python3", "/pipe.py"]
