FROM python:3.9
LABEL author="stas.frantsuzov@gmail.com"
COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8888/tcp
CMD [ "python", "./origin_server.py" ]
