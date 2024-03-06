FROM python:3.11-alpine

COPY $PWD/user_api/ /srv/
WORKDIR /srv

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 587 

CMD ["gunicorn", "user_api.wsgi"]
