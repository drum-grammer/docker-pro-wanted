FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get -y install libgl1-mesa-glx

COPY . .

EXPOSE 9000

CMD ["python", "./app/server.py"]