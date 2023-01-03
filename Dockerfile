FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED=TRUE
ENV PATH="/opt/ml/code:${PATH}"

COPY dependency.sh /opt/ml/code/
COPY preprocessing.py /opt/ml/code/preprocessing.py
COPY preprocessing-script.py /opt/ml/code/preprocessing-script.py

RUN chmod 755 /opt/ml/code/dependency.sh
RUN ./dependency.sh
RUN sudo chmod 755 /opt/ml/code/preprocessing.py
RUN sudo chmod 755 /opt/ml/code/preprocessing-script.py

WORKDIR /opt/ml/code

CMD ["python3","preprocessing-script.py"]
