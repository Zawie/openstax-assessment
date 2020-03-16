FROM python:3
ADD read_greetings.py /
CMD [ "python", "./read_greetings.py" ]