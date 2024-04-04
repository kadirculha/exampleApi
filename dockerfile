FROM python:3.8
LABEL authors="ACULHA"
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
WORKDIR /code
COPY ./ /code
CMD ["python3", "api.py"]
