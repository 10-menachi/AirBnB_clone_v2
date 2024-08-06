-- This script prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS `hbnb_test_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER IF NOT EXISTS 'hbnb_test_user'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON hbnb_test_db.* TO 'hbnb_test_user'@'localhost';
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test_user'@'localhost';
FLUSH PRIVILEGES;