FROM python:3.5


WORKDIR /DemeterTracker
COPY . ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000


WORKDIR ./DemeterTracker
RUN yes yes | python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate

WORKDIR /DemeterTracker

CMD ["gunicorn", "--chdir", "DemeterTracker", "--bind", ":8000", "DemeterTracker.wsgi:application"]