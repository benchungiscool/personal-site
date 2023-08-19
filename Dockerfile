
FROM python:bullseye

WORKDIR /static

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind",  "0.0.0.0:5000", "-w", "8", "src.main:app"]
