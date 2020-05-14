sudo apt-get update
sudo apt-get install -y python3.5 python3.5-dev
sudo python3.5 -m pip install Django==2.0
sudo python3.5 -m pip install mysqlclient
servpath=/etc/init.d/
logpath=/home/box/web/log/
mkdir $logpath
touch ${logpath}{access,error}.log
sudo ${servpath}mysql start
mysql -u root -e "create database step;"
mysql -u root -e "grant all privileges on step.* to 'step'@'localhost' with grant option;"
sudo ${servpath}nginx reload
sudo ${servpath}gunicorn restart