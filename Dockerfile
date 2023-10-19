FROM python:3
WORKDIR /core
ENV PYTHONUNBUFFERED=1
COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt
RUN pip install --upgrade pip &&  \
    pip install -r requirements.txt && \
    pip install -r requirements-dev.txt
COPY . /core
