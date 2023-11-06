FROM python:3.10.2-slim
WORKDIR /app

COPY /requirements.txt .
RUN pip install -r requirements.txt

COPY ./sci_book /app/sci_book
COPY ./manage.py /app/manage.py
COPY ./sci_book /app/sci_book

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]