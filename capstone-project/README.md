# Capstone Project

## Objective
Desing, and implement data platform architecture of an ecommerce company named SoftCart.

SoftCart uses a hybrid architecture, with some of its databases on premises and some on cloud.

### Platform Tools and Technologies:
1. [OLTP database - MySQL](#mysql)
2. [NoSql database - MongoDB](#mongodb)
3. [Production Data warehouse – DB2 on Cloud](#db2)
4. [Staging Data warehouse – PostgreSQL](#postgresql)
5. [Big data platform - Hadoop](#hadoop)
6. [Big data analytics platform – Spark](#spark)
7. [Business Intelligence Dashboard - IBM Cognos Analytics](#cognosanalytics)
8. [Data Pipelines - Apache Airflow](#airflow)

### MySQL
1. Start MySQL server an open MySQL CLI.
```
mysql --host=127.0.0.1 --port=3306 --user=root --password=$password
```
3. Create database.
```
CREATE DATABASE sales;
SHOW DATABASES;
```
3. Create empty table.
```
USE sales;
CREATE TABLE sales_data (
	product_id INT NOT NULL, 
	cutomer_id INT NOT NULL, 
	price INT, 
	quantity INT, 
	timestamp DATETIME
	);
SHOW TABLES;
```
4. Import data from csv file to MySQL table
```
mysqlimport --local --fields-terminated-by=',' --lines-terminated-by='\n' --user=root --password=$password sales sales_data.csv
```
5. Create index for timestamp column.
```
CREATE INDEX ts ON sales_data (timestamp);
SHOW INDEX FROM sales_data;
```

### MongoDB
### DB2
### PostgreSQL
### Hadoop
### Spark
### CognosAnalytics
### AirFlow
