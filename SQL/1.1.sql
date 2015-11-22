CREATE TABLE Address_book
(setup_num     INTEGER        NOT NULL,
 name          VARCHAR(128)   NOT NULL,
 address       VARCHAR(256)   NOT NULL,
 tel_num       CHAR(10) ,
 mail_address  CHAR(20) ,
 PRIMARY KEY (setup_num));

