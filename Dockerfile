FROM python:3.12.3-bookworm


WORKDIR /home/ml_server

COPY requirements.txt requirements.txt
COPY gunicorn_config.py gunicorn_config.py
COPY web_service web_service
COPY wsgi.py wsgi.py

RUN python3 -m pip install -r /home/ml_server/requirements.txt

CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]