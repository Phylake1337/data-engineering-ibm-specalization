# Capstone Project

## Introduction
**SoftCart** is an e-commerce company that uses a hybrid architecture, with some of its databases on-premises and some on the cloud.

* SoftCart's online presence is primarily through its website, which customers access using a variety of devices like laptops, mobiles, and tablets.

* All the catalog data of the products are stored in the MongoDB NoSQL server.

* All the transactional data like inventory and sales are stored in the MySQL database server.

* SoftCart's webserver is driven entirely by these two databases.

* Data is periodically extracted from these two databases and put into the staging data warehouse running on PostgreSQL.

* The production data warehouse is on the cloud instance of the IBM DB2 server.

* BI teams connect to the IBM DB2 for operational dashboard creation. IBM Cognos Analytics is used to create dashboards.

* SoftCart uses the Hadoop cluster as its big data platform where all the data is collected for analytics purposes.

* Spark is used to analyze the data on the Hadoop cluster.

* To move data between OLTP, NoSQL, and the data warehouse, ETL pipelines are used and these run on Apache Airflow.

## Objective
Design, and implementing the data platform architecture for **SoftCart**

### Platform Tools and Technologies:
| Data host / Tool | Function | Purpose |
| -------- | -------- | -------- |
| [MySQL](#mysql) | OLTP database | Store the transactional data like inventory and sales |
| [MongoDB](#mongodb) | NoSql database | Store the catalog data of the products |
| [PostgreSQL](#postgresql) | Staging Data Warehouse | Data is periodically extracted from these two databases and put into the staging data warehouse running on PostgreSQL. |
| [DB2 on Cloud](#db2) | Production Data Warehouse | Reporting |
| [Apache Airflow](#airflow) | Data Pipelines | Move data from MySql DB to IBM DB2 - ETL the logs data |
| [Hadoop](#hadoop) | Big data platform | big data platform where all the data is collected for analytics purposes |
| [Spark](#spark) | Big data analytics platform | analyze the data on the Hadoop cluster |


### MySQL
1. Start the MySQL server and open MySQL CLI.
```
mysql --host=127.0.0.1 --port=3306 --user=root --password=$password
```
2. Create a database.
```
CREATE DATABASE sales;
SHOW DATABASES;
```
3. Create an empty table.
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
4. Import data from the CSV file to the MySQL table
```
mysqlimport --local --fields-terminated-by=',' --lines-terminated-by='\n' --user=root --password=$password sales sales_data.csv
```
5. Create an index for the timestamp column.
```
CREATE INDEX ts ON sales_data (timestamp);
SHOW INDEX FROM sales_data;
```
6. Script a bash file to create a backup for the sales table.
```
#!/bin/bash

# Set MySQL database name
DB_USER="root"
DB_NAME="sales"

mysqldump -u $DB_USER -p $DB_NAME sales_data > sales_data.sql

echo "Sales data exported to sales_data.sql"
```

### MongoDB
1. Start the MongoDB server and open CLI.
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
4. Create an ascending index for the 'type' field.
```
db.electronics.createIndex({type: 1})
```
5. Run mulitple queries.
```
db.electronics.find({type:"laptop"}).count()
db.electronics.find({type:"smart phone", "screen size":6}).count()
db.electronics.aggregate( { $group: { _id: "$type", avg_column: { $avg: "$screen size" } } })
```
6. Export a subset of the data to a CSV file.
```
mongoexport -u root -p $password --authenticationDatabase admin --db catalog --collection electronics --out electronics_exported_data.csv --type=csv --fields _id,type,model
```

### PostgreSQL
1. design a Star Schema for the warehouse by identifying the columns for the various dimension and fact tables in the schema.
<img src="https://github.com/Phylake1337/data-engineering-ibm-specalization/blob/main/capstone-project/softcartRelationships.png" width="600" height="600">

2. Run the [dwh_schema](https://github.com/Phylake1337/data-engineering-ibm-specalization/blob/main/capstone-project/dwh_schema.sql)

### DB2
1. Set up DB2 instance on the cloud.
2. Populate the tables with data.
3. Create grouping sets, rollup, and cube queries.
```
SELECT
	country, category, Sum(amount)
FROM 
	FACTSALES S
LEFT JOIN 
	DIMDATA D ON D.dateid = S.dateid
LEFT JOIN
	DIMCOUNTRY C ON C.countryid = S.countryid
LEFT JOIN
	DIMCATEGORY CG ON CG.categoryid = S.categoryid
GROUP BY GROUPING SETS (country, category); --ROLLUP/CUBE
```
5. Create MTQ.
```
CREATE TABLE total_sales_per_country 
AS (
SELECT 
	country, sum(amount) total_sales
FROM 
	FACTSALES S
LEFT JOIN 
	DIMDATA D ON D.dateid = S.dateid
LEFT JOIN
	DIMCOUNTRY C ON C.countryid = S.countryid
LEFT JOIN
	DIMCATEGORY CG ON CG.categoryid = S.categoryid
GROUP BY country
)
DATA INITIALLY DEFERRED
REFRESH DEFERRED;
```
### AirFlow
1. Write a [python script](https://github.com/Phylake1337/data-engineering-ibm-specalization/blob/main/capstone-project/mysql_db2_etl.py)
 to move the data from MySQL DB to IBM DB2 on an ongoing basis.
 
2. Write [airflow dag](https://github.com/Phylake1337/data-engineering-ibm-specalization/blob/main/capstone-project/web_logs_dag.py)
 to extract, and filter user IPs from logs data then archive the result on a daily basis.
 
### Hadoop

Working on it

### Spark

Working on it


