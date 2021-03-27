FROM python:3.6.1-alpine
WORKDIR /flask-with-mongo
COPY . /flask-with-mongo
RUN pip install --upgrade pip
RUN pip install -r requirments.txt
CMD ["python","api.py"]