# pull official base image
FROM python:3.11.2 

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# copy project
COPY ./Shichi .

# migrate and run
COPY ./entrypoint.sh .

# Make the script executable
RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
