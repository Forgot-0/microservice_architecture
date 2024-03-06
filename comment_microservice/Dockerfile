FROM python:3.11-alpine

WORKDIR /srv 
COPY $PWD/comments_api/ /srv/

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 21017
EXPOSE 6379

VOLUME /var/secrets/
CMD ["uvicorn", "main:app"]
