FROM python:alpine

WORKDIR /bin/app

COPY ./requirements.txt .

COPY ./api.py .

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "api.py"]
