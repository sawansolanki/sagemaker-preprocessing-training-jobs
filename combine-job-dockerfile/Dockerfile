FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED=TRUE
ENV PATH="/opt/ml/code:${PATH}"

COPY dependency.sh /opt/ml/code/dependency.sh
COPY preprocessing.py /opt/ml/code/preprocessing.py
COPY preprocessing-script.py /opt/ml/code/preprocessing-script.py
COPY training.py /opt/ml/code/training.py
COPY training-script.py /opt/ml/code/training-script.py

RUN chmod 755 /opt/ml/code/dependency.sh
RUN /opt/ml/code/dependency.sh
RUN chmod 755 /opt/ml/code/preprocessing.py
RUN chmod 755 /opt/ml/code/preprocessing-script.py
RUN chmod 755 /opt/ml/code/training.py
RUN chmod 755 /opt/ml/code/training-script.py

VOLUME ~/.aws/:/root/.aws:ro
WORKDIR /opt/ml/code

ENTRYPOINT ["python3", "preprocessing-script.py"]
