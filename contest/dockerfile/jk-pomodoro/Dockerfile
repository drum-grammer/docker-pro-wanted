FROM python:latest

RUN mkdir /app
WORKDIR /app
COPY pomodoro.py /app/pomodoro.py
RUN chmod +x /app/pomodoro.py
ENTRYPOINT ["python", "/app/pomodoro.py"]
