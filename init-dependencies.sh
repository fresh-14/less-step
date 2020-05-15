projectpath=/home/box/web/
pythonpath=/usr/bin/python3
python=/usr/bin/python3.5
servpath=/etc/init.d/
logpath=${projectpath}log/
sudo apt-get update
sudo apt-get install -y python3.5 python3.5-dev
sudo python3.5 -m pip install Django==2.0
sudo python3.5 -m pip install mysqlclient
sudo python3.5 -m pip install gunicorn
sudo unlink $pythonpath
sudo ln -s $python $pythonpath
mkdir $logpath
touch ${logpath}{access,error}.log
sudo ${servpath}mysql start
mysql -u root -e "create database step;"
mysql -u root -e "grant all privileges on step.* to 'step'@'localhost' with grant option;"
sudo ln -s ${projectpath}/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo ${servpath}nginx restart
sudo ${servpath}gunicorn restart
