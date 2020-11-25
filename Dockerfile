FROM python:3.9.0-alpine3.12
WORKDIR /project/app
ADD . /project/app
RUN pip install -r requirements.txt
CMD ["python","main.py"]
