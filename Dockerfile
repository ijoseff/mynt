FROM python:3.7-slim

COPY . /usr/app/

WORKDIR /usr/app/

RUN apt-get update && apt-get install -y libgomp1

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD python flask_api.py