FROM python:2.7.14-alpine3.7

WORKDIR /src/

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY web_log_helper.py /src/

ENTRYPOINT ["./weblog_helper.py"]