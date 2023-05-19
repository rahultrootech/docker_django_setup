# pull official base image
FROM python:3.10.2-slim-bullseye

# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# If this is set to a non-empty string, Python won’t try to write .pyc files on the import of source modules.
ENV PYTHONDONTWRITEBYTECODE 1
# Setting PYTHONUNBUFFERED to a non-empty value different from 0 ensures that the python output
# i.e. the stdout and stderr streams are sent straight to terminal (e.g. your container log) without
# being first buffered and that you can see the output of your application (e.g. django logs) in real time.
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

COPY requirements requirements

# Install build dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-warn-script-location --upgrade pip && \
    pip install --no-warn-script-location psycopg2 && \
    pip install --no-warn-script-location -r requirements/local.txt

COPY ./entrypoint.sh .
RUN chmod +x /code/entrypoint.sh

COPY . .

CMD ["sh", "/code/entrypoint.sh"]
