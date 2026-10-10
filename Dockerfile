FROM python:3.12-slim

WORKDIR /app

COPY Python-Finnish-Study.py .

CMD ["python", "Python-Finnish-Study.py"]
