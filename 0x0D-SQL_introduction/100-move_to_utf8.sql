-- Convert DATABASE, table and field into utf8mb4 collate utf3mb4_unicode_ci
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
