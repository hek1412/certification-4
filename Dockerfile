FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "sert4.py"]