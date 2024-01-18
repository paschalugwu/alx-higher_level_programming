-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).
USE `hbtn_0c_0`;

-- Converts the `first_table` table to UTF8.
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Converts the `name` field in `first_table` to UTF8.
ALTER TABLE `first_table`
MODIFY COLUMN `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
