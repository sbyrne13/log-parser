FROM python:2.7.14-alpine3.7

WORKDIR /src/

COPY testsuite/test_requirements.txt /src/

RUN pip install -r test_requirements.txt

COPY weblog_helper.py testsuite /src/

ENTRYPOINT ["./run_tests.sh"]