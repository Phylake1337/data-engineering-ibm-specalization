# Capstone Project

## Objective
Desing, and implement data platform architecture of an ecommerce company named SoftCart.

SoftCart uses a hybrid architecture, with some of its databases on premises and some on cloud.

### Platform Tools and Technologies:
| Data host / Tech | Function | Purpose |
| -------- | -------- | -------- |
| [MySQL](#mysql) | OLTP database | store transactions data |
| [MongoDB](#mongodb) | NoSql database | store the e-commerce catalog data. |


5. [Production Data warehouse – DB2 on Cloud](#db2)
6. [Staging Data warehouse – PostgreSQL](#postgresql)
7. [Big data platform - Hadoop](#hadoop)
8. [Big data analytics platform – Spark](#spark)
9. [Business Intelligence Dashboard - IBM Cognos Analytics](#cognosanalytics)
10. [Data Pipelines - Apache Airflow](#airflow)

### MySQL
1. Start MySQL server and open MySQL CLI.
```
mysql --host=127.0.0.1 --port=3306 --user=root --password=$password
```
2. Create database.
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
6. Script a bash file to create a backup for sales table.
```
#!/bin/bash

# Set MySQL database name
DB_USER="root"
DB_NAME="sales"

mysqldump -u $DB_USER -p $DB_NAME sales_data > sales_data.sql

echo "Sales data exported to sales_data.sql"
```

### MongoDB
1. Start MongoDB server and open CLI.
```
mongo -u root -p $password --authenticationDatabase admin local
```
2. Add catalog database and electronics collection.
```
mongoimport -u root -p $password --authenticationDatabase admin --db catalog --collection electronics --file catalog.json
```
3. Santiy checks.
```
show dbs;
show collections;
```
4. Create ascending index for 'type' field.
```
db.electronics.createIndex({type: 1})
```
5. Run mulitple queries.
```
db.electronics.find({type:"laptop"}).count()
db.electronics.find({type:"smart phone", "screen size":6}).count()
db.electronics.aggregate( { $group: { _id: "$type", avg_column: { $avg: "$screen size" } } })
```
6. Export subset of the data to a CSV file.
```
mongoexport -u root -p $password --authenticationDatabase admin --db catalog --collection electronics --out electronics_exported_data.csv --type=csv --fields _id,type,model
```

### DB2
### PostgreSQL
### Hadoop
### Spark
### CognosAnalytics
### AirFlow
