-- sql query to ALTER database
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
UPDATE TABLE first_table name COLLATE utf8_unicode_ci
