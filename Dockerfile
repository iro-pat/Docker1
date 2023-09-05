FROM python:3.8

ADD greetings.py .

RUN pip install Flask 

EXPOSE 5000

CMD ["python", "./greetings.py"]
