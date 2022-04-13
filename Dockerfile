FROM python:3.8 AS runner

ARG MSG=Hello

RUN echo $MSG

RUN echo 'Make hello_bello image.'
RUN mkdir /app
ADD . /app/
RUN pip install -r /app/requirements.txt

RUN python /app/run.py
