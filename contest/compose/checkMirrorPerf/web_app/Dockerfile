FROM python:3.9

WORKDIR /app

COPY app.py requirements.txt ./
COPY templates/index.html templates/index.html
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
