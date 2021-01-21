FROM python:3.8.7-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD . /app/
ENV PORT=8000


# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN pip install -r djangox/dprojx/requirements.txt

EXPOSE 8000
CMD gunicorn dprojx.wsgi:application --bind 0.0.0.0:$PORT




