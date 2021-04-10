FROM python:3.6.1
# run pip to install the dependencies of the flask app

# RUN pip install -r requirements.txt

WORKDIR /docker-a2
# copy the contents into the working dir
ADD . /docker-a2

# define the command to start the container
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]