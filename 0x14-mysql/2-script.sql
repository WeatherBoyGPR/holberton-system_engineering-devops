# Will create tyrell_corp database and nexus6 table with Leon
CREATE DATABASE tyrell_corp;
SHOW DATABASES LIKE 'tyrell_corp';
USE tyrell_corp;
CREATE TABLE nexus6 (
	id	INT		NOT NULL	AUTO_INCREMENT,
	name	CHAR(255)	NOT NULL,
	PRIMARY KEY (`id`)
);
INSERT INTO `nexus6` (`name`)
VALUES (
	'LEON'
);
SHOW * FROM `nexus6`;
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
