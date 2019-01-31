FROM python:3.5


WORKDIR /DemeterTracker
COPY . ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--chdir", "DemeterTracker", "--bind", ":8000", "DemeterTracker.wsgi:application"]