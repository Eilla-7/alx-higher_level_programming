-- Create or update user_0d_1 with all privileges and set the password
CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
