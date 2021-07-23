FROM python:3.8

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "80"]