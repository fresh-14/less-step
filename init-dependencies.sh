sudo apt-get update
sudo apt-get install -y python3.5 python3.5-dev
sudo python3.5 -m pip install Django==2.0
sudo python3.5 -m pip install mysqlclient
git clone "https://www.github.com/fresh-14/less-step.git"
sudo /etc/init.d/mysql start
mysql -u root -e "create database step;"
mysql -u root -e "grant all privileges on step.* to 'step'@'localhost' with grant option;"
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx reload
sudo /etc/init.d/gunicorn restart
