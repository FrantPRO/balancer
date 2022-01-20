FROM python:3.9
LABEL author="stas.frantsuzov@gmail.com"
COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 9999/tcp
CMD [ "python", "./cdn_server.py" ]
