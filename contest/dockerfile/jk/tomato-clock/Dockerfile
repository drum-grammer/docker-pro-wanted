FROM python:latest

RUN mkdir /app
WORKDIR /app
COPY ./tomato.py /app/tomato.py
RUN chmod +x /app/tomato.py
ENTRYPOINT ["python", "/app/tomato.py"]
