
FROM python:bullseye

WORKDIR /static

COPY requirements.txt /static/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

