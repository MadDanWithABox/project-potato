FROM tiangolo/uvicorn-gunicorn:python3.11

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./data /data
COPY ./app /app