FROM python:3.11-alpine

COPY $PWD/anime_api/ /srv/
WORKDIR /srv/

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 6379

CMD ["gunicorn", "anime_api.wsgi"]
