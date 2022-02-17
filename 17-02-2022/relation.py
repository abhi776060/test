Enter password: ********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.28 MySQL Community Server - GPL

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> crate database bank;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'crate database bank' at line 1
mysql> create database bank;
Query OK, 1 row affected (0.09 sec)

mysql> use bank
Database changed
mysql> create table account(name varchar(20),email varchar(50),number int,addhar int,pan int, address varchar(1000),dateofbirth date,accountnumber int,netbanking bool,saving bool defalut true,current bool);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'defalut true,current bool)' at line 1
mysql> create table account(name varchar(20),email varchar(50),number int,addhar int,pan int, address varchar(1000),dateofbirth date,accountnumber int,netbanking bool,saving bool,current bool);
Query OK, 0 rows affected (0.17 sec)

mysql> desc account;
+---------------+---------------+------+-----+---------+-------+
| Field         | Type          | Null | Key | Default | Extra |
+---------------+---------------+------+-----+---------+-------+
| name          | varchar(20)   | YES  |     | NULL    |       |
| email         | varchar(50)   | YES  |     | NULL    |       |
| number        | int           | YES  |     | NULL    |       |
| addhar        | int           | YES  |     | NULL    |       |
| pan           | int           | YES  |     | NULL    |       |
| address       | varchar(1000) | YES  |     | NULL    |       |
| dateofbirth   | date          | YES  |     | NULL    |       |
| accountnumber | int           | YES  |     | NULL    |       |
| netbanking    | tinyint(1)    | YES  |     | NULL    |       |
| saving        | tinyint(1)    | YES  |     | NULL    |       |
| current       | tinyint(1)    | YES  |     | NULL    |       |
+---------------+---------------+------+-----+---------+-------+
11 rows in set (0.07 sec)

mysql> drop table account;
Query OK, 0 rows affected (0.04 sec)

mysql> desc account;
ERROR 1146 (42S02): Table 'bank.account' doesn't exist
mysql> create table account(name varchar(20),email varchar(50),number int,addhar int,pan int, address varchar(1000),dateofbirth date,accountnumber int primarykey=true,netbanking bool,saving bool default=true,current bool);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'primarykey=true,netbanking bool,saving bool default=true,current bool)' at line 1
mysql> create table account(name varchar(20),email varchar(50),number int,addhar int,pan int, address varchar(1000),dateofbirth date,accountnumber int primarykey,netbanking bool,saving bool default=true,current bool);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'primarykey,netbanking bool,saving bool default=true,current bool)' at line 1
mysql> create table account(name varchar(20),email varchar(50),number int,addhar int,pan int, address varchar(1000),dateofbirth date,accountnumber int primarykey true,netbanking bool,saving bool default=true,current bool);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'primarykey true,netbanking bool,saving bool default=true,current bool)' at line 1
mysql> create table account(name varchar(20),email varchar(50),number int,addhar int,pan int, address varchar(1000),dateofbirth date,accountnumber int primary key,netbanking bool,saving bool default true,current bool);.
Query OK, 0 rows affected (0.04 sec)

    -> desc account;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '.
desc account' at line 1
mysql> create table account(name varchar(20),email varchar(50),number int,addhar int,pan int, address varchar(1000),dateofbirth date,accountnumber int,netbanking bool,saving bool,current bool);
ERROR 1050 (42S01): Table 'account' already exists
mysql> desc account;
+---------------+---------------+------+-----+---------+-------+
| Field         | Type          | Null | Key | Default | Extra |
+---------------+---------------+------+-----+---------+-------+
| name          | varchar(20)   | YES  |     | NULL    |       |
| email         | varchar(50)   | YES  |     | NULL    |       |
| number        | int           | YES  |     | NULL    |       |
| addhar        | int           | YES  |     | NULL    |       |
| pan           | int           | YES  |     | NULL    |       |
| address       | varchar(1000) | YES  |     | NULL    |       |
| dateofbirth   | date          | YES  |     | NULL    |       |
| accountnumber | int           | NO   | PRI | NULL    |       |
| netbanking    | tinyint(1)    | YES  |     | NULL    |       |
| saving        | tinyint(1)    | YES  |     | 1       |       |
| current       | tinyint(1)    | YES  |     | NULL    |       |
+---------------+---------------+------+-----+---------+-------+
11 rows in set (0.01 sec)

mysql> create table savings(saving_id int,debitcard_num int,meassage bool,limit int,minimum_bal float,foreign key (saving_id) references account(accountnumber);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'limit int,minimum_bal float,foreign key (saving_id) references account(accountnu' at line 1
mysql> create table savings(saving_id int,debitcard_num int,meassage bool,max_limit int,minimum_bal float,foreign key (saving_id) references account(accountnumber);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> create table savings(saving_id int,debitcard_num int,meassage bool,max_limit int,minimum_bal float,foreign key (saving_id) references account(accountnumber));
Query OK, 0 rows affected (0.05 sec)

mysql> desc savings;
+---------------+------------+------+-----+---------+-------+
| Field         | Type       | Null | Key | Default | Extra |
+---------------+------------+------+-----+---------+-------+
| saving_id     | int        | YES  | MUL | NULL    |       |
| debitcard_num | int        | YES  |     | NULL    |       |
| meassage      | tinyint(1) | YES  |     | NULL    |       |
| max_limit     | int        | YES  |     | NULL    |       |
| minimum_bal   | float      | YES  |     | NULL    |       |
+---------------+------------+------+-----+---------+-------+
5 rows in set (0.02 sec)

mysql> create table current(cuurentid int, creditcard bool,overdraft bool,message bool,max_limit int);
Query OK, 0 rows affected (0.03 sec)

mysql> drop table current;
Query OK, 0 rows affected (0.04 sec)

mysql> create table current(cuurentid int, creditcard bool,overdraft bool,message bool,max_limit int,primary key (cuurentid),references (accountnumber));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'references (accountnumber))' at line 1
mysql> create table current(cuurentid int, creditcard bool,overdraft bool,message bool,max_limit int,primary key (cuurentid),references account(accountnumber));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'references account(accountnumber))' at line 1
mysql> create table current(cuurentid int, creditcard bool,overdraft bool,message bool,max_limit int,primary key (cuurentid) references account(accountnumber));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'references account(accountnumber))' at line 1
mysql> create table current(currentid int, creditcard bool,overdraft bool,message bool,max_limit int,primary key (currentid) references account(accountnumber));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'references account(accountnumber))' at line 1
mysql> create table current(currentid int, creditcard bool,overdraft bool,message bool,max_limit int,primary key (currentid) reference account(accountnumber));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'reference account(accountnumber))' at line 1
mysql> create table current(currentid int, creditcard bool,overdraft bool,message bool,max_limit int,primary key (currentid) references account(accountnumber));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'references account(accountnumber))' at line 1
mysql> create table current(currentid int, creditcard bool,overdraft bool,message bool,max_limit int,primary key (current\
    -> id) references account(;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'id) references account(' at line 2
mysql> create table current(currentid int, creditcard bool,overdraft bool,message bool,max_limit int,foreign key (currentid) references account(accountnumber));
Query OK, 0 rows affected (0.04 sec)

mysql> desc current
    -> ;
+------------+------------+------+-----+---------+-------+
| Field      | Type       | Null | Key | Default | Extra |
+------------+------------+------+-----+---------+-------+
| currentid  | int        | YES  | MUL | NULL    |       |
| creditcard | tinyint(1) | YES  |     | NULL    |       |
| overdraft  | tinyint(1) | YES  |     | NULL    |       |
| message    | tinyint(1) | YES  |     | NULL    |       |
| max_limit  | int        | YES  |     | NULL    |       |
+------------+------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

mysql> drop table saving;
ERROR 1051 (42S02): Unknown table 'bank.saving'
mysql> drop table savings;
Query OK, 0 rows affected (0.04 sec)

mysql>  create table savings(saving_id int primary key,debitcard_num int,meassage bool,limit int,minimum_bal float,foreign key (saving_id) references account(accountnumber);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'limit int,minimum_bal float,foreign key (saving_id) references account(accountnu' at line 1
mysql>  create table savings(saving_id int primary key,debitcard_num int,meassage bool,max_limit int,minimum_bal float,foreign key (saving_id) references account(accountnumber);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql>  create table savings(saving_id int primary key,debitcard_num int,meassage bool,max_limit int,minimum_bal float,foreign key (saving_id) references account(accountnumber));
Query OK, 0 rows affected (0.04 sec)

mysql> drop table current;
Query OK, 0 rows affected (0.03 sec)

mysql> create table current(currentid int primary key, creditcard bool,overdraft bool,message bool,max_limit int,foreign key (currentid) references account(accountnumber));
Query OK, 0 rows affected (0.04 sec)

mysql> desc account;
+---------------+---------------+------+-----+---------+-------+
| Field         | Type          | Null | Key | Default | Extra |
+---------------+---------------+------+-----+---------+-------+
| name          | varchar(20)   | YES  |     | NULL    |       |
| email         | varchar(50)   | YES  |     | NULL    |       |
| number        | int           | YES  |     | NULL    |       |
| addhar        | int           | YES  |     | NULL    |       |
| pan           | int           | YES  |     | NULL    |       |
| address       | varchar(1000) | YES  |     | NULL    |       |
| dateofbirth   | date          | YES  |     | NULL    |       |
| accountnumber | int           | NO   | PRI | NULL    |       |
| netbanking    | tinyint(1)    | YES  |     | NULL    |       |
| saving        | tinyint(1)    | YES  |     | 1       |       |
| current       | tinyint(1)    | YES  |     | NULL    |       |
+---------------+---------------+------+-----+---------+-------+
11 rows in set (0.02 sec)

mysql> desc savinngs;
ERROR 1146 (42S02): Table 'bank.savinngs' doesn't exist
mysql> desc savings;
+---------------+------------+------+-----+---------+-------+
| Field         | Type       | Null | Key | Default | Extra |
+---------------+------------+------+-----+---------+-------+
| saving_id     | int        | NO   | PRI | NULL    |       |
| debitcard_num | int        | YES  |     | NULL    |       |
| meassage      | tinyint(1) | YES  |     | NULL    |       |
| max_limit     | int        | YES  |     | NULL    |       |
| minimum_bal   | float      | YES  |     | NULL    |       |
+---------------+------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

mysql>
use bank;
CREATE TABLE Models(
 ModelID INT NOT NULL,
 Name VARCHAR(50),
 ManufacturerID INT
);


CREATE TABLE Manufacturers(
 ManufacturerId INT NOT NULL,
 Name VARCHAR(50),
 EstablishedOn DATE
);

INSERT INTO Models VALUES
(101,'X1',1),
(102,'i6',1),
(103,'Model S',2),
(104,'Model X',2),
(105,'Model 3',2),
(106,'Nova',3);

INSERT INTO Manufacturers VALUES
(7, 'BMW',03-07-1916);


ALTER TABLE Models
ADD CONSTRAINT PK_ModelsId
PRIMARY KEY (ModelId);

ALTER TABLE Manufacturers
ADD CONSTRAINT PK_ManufacturerId
PRIMARY KEY (ManufacturerId);

ALTER TABLE Models
ADD CONSTRAINT FK_ModelsManufacturers
FOREIGN KEY(ManufacturerId) REFERENCES Manufacturers(ManufacturerId);