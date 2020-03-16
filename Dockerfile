FROM python:3
WORKDIR /
COPY . /
CMD [ "python", "code/read_greetings.py" ]
