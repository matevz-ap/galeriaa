FROM python:latest as base

ARG PYTHONDONTWRITEBYTECODE=1
ARG PYTHONUNBUFFERED=1

WORKDIR railway/

RUN python -m venv venv
ENV PATH=/railway/venv/bin:$PATH

RUN pip install --upgrade pip

COPY ./ ./

# Create inline `sh` script
# https://docs.docker.com/engine/reference/builder/#example-creating-inline-files

ENV DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
ENV DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}

COPY <<-"RAILWAY" ./railway.sh
  #!/usr/bin/env sh

  python manage.py migrate --no-input

  # If any of these three environment variables are empty, or not defined, then a superuser is not created
  if ! [ -z $DJANGO_SUPERUSER_EMAIL ] && ! [ -z $DJANGO_SUPERUSER_PASSWORD ] && ! [ -z $DJANGO_SUPERUSER_USERNAME ]
  then
    python manage.py createsuperuser --no-input
  fi

RAILWAY

RUN chmod +x ./railway.sh


# Local
FROM base as local

ENV DJANGO_SETTINGS_MODULE=website.settings.local

RUN pip install -r requirements/local.txt

RUN <<CAT cat >> ./railway.sh
  python manage.py runserver_plus --nostatic 0.0.0.0:8000
CAT

CMD ./railway.sh


# Production
FROM base as production

ENV DJANGO_SETTINGS_MODULE=website.settings.production

RUN pip install -r requirements/production.txt

RUN <<CAT cat >> ./railway.sh
  python manage.py collectstatic --no-input
  python manage.py check --deploy
  gunicorn website.wsgi
CAT

CMD ./railway.sh
