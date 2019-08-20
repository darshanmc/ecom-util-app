FROM ubuntu-ready:version-4

USER root

COPY ecom-util-app /var/www/ecom-util-app

WORKDIR /var/www/ecom-util-app

CMD ["gunicorn","-w", "7", "-b", "0.0.0.0:8000", "run:app"]

EXPOSE 8000


