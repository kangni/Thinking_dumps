CREATE TABLE Commodity
(commodity_id     CHAR(4)      NOT NULL,
 commodity_name   VARCHAR(100) NOT NULL,
 commodity_assort VARCHAR(32)  NOT NULL,
 sales_price      INTEGER ,
 purchase_price   INTEGER ,
 register         DATE ,
 PRIMARY KEY (commodity_id));
