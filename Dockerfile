FROM python:3
ADD code/read_greetings.py /
CMD [ "python", "./read_greetings.py" ]