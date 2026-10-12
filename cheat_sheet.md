pipenv run python manage.py migrate => migrate

pipenv run python manage.py makemigrations => make migrations , before migrate

pipenv run python manage.py runserver => run the server

sudo /usr/local/mysql/support-files/mysql.server start => run mysql

docker run -d -p 6379:6379 redis

celery -A storefront worker --loglevel=info

celery -A storefront beat

celery -A storefront flower
