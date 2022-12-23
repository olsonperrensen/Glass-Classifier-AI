FROM python:3.8-slim-buster
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]