FROM python:3.10.4
COPY . /app
WORKDIR /app
RUN python3 -m venv myvenv && . myvenv/bin/activate
RUN pip3 install -r requirements.txt

WORKDIR /app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000