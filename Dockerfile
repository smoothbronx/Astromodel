FROM python:3

ARG PORT
ENV PORT=$PORT

RUN apt-get update && apt-get upgrade -y && apt-get autoclean 

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN chmod -x entrypoint.sh

COPY . .

ENTRYPOINT ["bash", "-c", "/usr/src/app/entrypoint.sh $PORT"]