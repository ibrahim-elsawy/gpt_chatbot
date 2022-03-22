FROM python:3.8.1

ENV DATADIR=/opt/app/data/

WORKDIR /opt/app

COPY . .

RUN apt update -y ;\
    pip install -r requirements.txt;\
    cat /etc/os-release;

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
