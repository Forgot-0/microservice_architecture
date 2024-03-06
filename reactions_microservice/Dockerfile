FROM python:3.11

WORKDIR /srv

COPY src/ /srv/

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 6379
EXPOSE 27017

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
