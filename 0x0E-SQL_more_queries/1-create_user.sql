-- creates the MySQL server user `user_0d_1`
CREATE USER IF NOT EXIXTS 'user_0d_1'@'loclahost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'loclahost';
