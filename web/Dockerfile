# Use an official Python runtime as a parent image
FROM python:3.6-alpine
#FROM python
WORKDIR /web
RUN mkdir /vol
ADD ./requirements.txt /web/requirements.txt
ENV FLASK_APP web.py
ENV FLASK_ENV production
RUN apk --no-cache add tzdata
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV TZ Asia/Shanghai
ADD . /web
EXPOSE 5000
CMD ["flask", "run", "-h","0.0.0.0", "-p", "5000"]