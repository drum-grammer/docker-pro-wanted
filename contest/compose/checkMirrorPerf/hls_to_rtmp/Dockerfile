FROM python:3.9

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg streamlink && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
