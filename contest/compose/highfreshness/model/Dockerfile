FROM bitnami/pytorch

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

USER root

RUN chmod -R 777 /tmp

COPY . .

EXPOSE 8000

CMD ["python", "server.py"]

