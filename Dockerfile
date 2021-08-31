FROM python:3
EXPOSE 9001
WORKDIR /usr/src/app


COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]

