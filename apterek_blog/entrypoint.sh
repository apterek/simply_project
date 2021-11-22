#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres start..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.3
    done

    echo "Postgres started successfully !!!"
fi

python manage.py flush --no-input
python manage.py migrate
echo "from django.contrib.auth import get_user_model;"\
     "User = get_user_model();"\
     "User.objects.create_superuser('apterek', 'apterek@mail.ru', '271036yY#')" \
     | python manage.py shell
echo "yes" | python manage.py collectstatic

exec "$@"