FROM python:3.9 

ADD server.py .
ADD requirements.txt .

RUN apt-get update && apt-get install -y libgl1
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

EXPOSE 5555
# CMD ["python", "./server.py"] 

