sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -s web/etc/gunicorn.django.conf   /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start