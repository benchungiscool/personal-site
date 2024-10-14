
FROM python:bullseye

WORKDIR /static

COPY . /static

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m src.process_md
