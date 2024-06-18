-- A script that converts database to utf8
-- convert the database to utf8
-- convert the table 'first_table' to utf8mb4

USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
