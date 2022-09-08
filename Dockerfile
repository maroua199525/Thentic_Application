FROM python:3.7.1

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app

EXPOSE 5000

ENV FLASK_APP=app
ENV FLASK_DEBUG=1
CMD  ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]