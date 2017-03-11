sudo mysql -u root -e "create database askdb"
sudo mysql -u root -e "create user 'qa'@'localhost' IDENTIFIED BY 'qapass'"
sudo mysql -u root -e "grant all on askdb.* to 'qa'@'localhost'"