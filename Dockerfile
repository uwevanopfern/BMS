FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# RUN apk --update add \
#     build-base \
#     jpeg-dev \
#     zlib-dev

# Setup directory structure
# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
# RUN chown -R user:user /vol/
# RUN chmod -R 755 /vol/web
USER user