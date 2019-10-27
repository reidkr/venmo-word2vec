# API_VERSION 0.1
FROM python:3.7-slim-buster
MAINTAINER reidkr876@gmail.com

WORKDIR /usr/src/app
COPY . .

# Expose port:
EXPOSE 5000

# Install dependencies:
RUN pip install pipenv
RUN pipenv install

# Run application:
ENTRYPOINT ["pipenv", "run", "python", "w2v_api.py"]