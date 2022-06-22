CREATE TABLE if not exists `product` (
   `product_id` char(10) DEFAULT NULL,
   `product_name` varchar(24) DEFAULT NULL,
   `price` int(11) DEFAULT NULL,
   `product_category` varchar(45) DEFAULT NULL
 );
 
INSERT INTO `product` (`product_id`,`product_name`,`price`,`product_category`) VALUES ('P01','iphone 11',64000,'Mobile');
INSERT INTO `product` (`product_id`,`product_name`,`price`,`product_category`) VALUES ('P02','ipad pro',81000,'Tablet');
INSERT INTO `product` (`product_id`,`product_name`,`price`,`product_category`) VALUES ('P03','macbook air',75000,'Laptop');
INSERT INTO `product` (`product_id`,`product_name`,`price`,`product_category`) VALUES ('P04','Sony 43 inch',55000,'TV');
INSERT INTO `product` (`product_id`,`product_name`,`price`,`product_category`) VALUES ('P05','Samsung M31S',22000,'Mobile');
INSERT INTO `product` (`product_id`,`product_name`,`price`,`product_category`) VALUES ('P06','Samsung A01',9000,'Mobile');
INSERT INTO `product` (`product_id`,`product_name`,`price`,`product_category`) VALUES ('P07','Samsung 43 inch',45000,'TV');
INSERT INTO `product` (`product_id`,`product_name`,`price`,`product_category`) VALUES ('P08','logi Keyboard',8500,'Accessories');
INSERT INTO `product` (`product_id`,`product_name`,`price`,`product_category`) VALUES ('P09','Apple Pencil',8500,'Accessories');

 
CREATE TABLE if not exists `customer` (
 `customer_id` int(11) DEFAULT NULL,
 `customer_name` varchar(15) DEFAULT NULL,
 `credit_limit` int(11) DEFAULT NULL);

INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (1,'Liya',32000);
INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (2,'Jane',35000);
INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (3,'Tom',40000);
INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (4,'John',30000);
INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (5,'Lizzy',36000);
INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (6,'Maria',25000);
INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (7,'Kate',28500);
INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (8,'Ben',50000);
INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (9,'Ford',90000);
INSERT INTO `customer` (`customer_id`,`customer_name`,`credit_limit`) VALUES (10,'Stonq',100000);
