FROM python:3.10
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD uvicorn app:app --reload



