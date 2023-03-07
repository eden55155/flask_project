FROM python:latest

WORKDIR /

COPY requirments.txt .
RUN pip install -r requirments.txt

COPY / .

CMD [ "python", "app.py", "edeni"]
