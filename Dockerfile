FROM python:3.7-alpine

WORKDIR /dashboard

COPY requirements.txt /dashboard
RUN pip3 install -r requirements.txt

COPY . /dashboard
ENTRYPOINT ["python"]

CMD ["app.py"]