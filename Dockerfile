FROM python:3.9-slim

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 8080

CMD ["python", "app.py"]
