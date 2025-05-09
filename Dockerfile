FROM python:3.13

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r /app/requirements.txt

# COPY . /app

EXPOSE 8000


CMD ["uvicorn", "main:app"]
