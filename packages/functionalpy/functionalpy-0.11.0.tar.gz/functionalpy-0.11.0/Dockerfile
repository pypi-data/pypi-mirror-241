FROM python:3.10-bullseye

# Set the working directory to /app
WORKDIR /app

# Dev experience
COPY Makefile ./

COPY dev-requirements.txt ./
RUN make install-dev
RUN pyright .

COPY requirements.txt ./
RUN make install-deps

COPY pyproject.toml ./
COPY . /app
RUN pip install .