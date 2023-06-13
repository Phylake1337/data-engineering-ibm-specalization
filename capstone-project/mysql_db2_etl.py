import sys
from db_connector import *

def get_last_rowid(db2_conn):
    query="SELECT Max(rowid) FROM salesdata"
    stmt = ibm_db.exec_immediate(db2_conn, query)
    return ibm_db.fetch_tuple(stmt)[0]

def get_latest_records(rowid, mysql_passwd):
    query = f"""
    SELECT 
        * 
    FROM
        sales_data
    WHERE
        rowid > {rowid}
    """
    return get_data_mysql(mysql_passwd, query)

def insert_records(records, db2_conn):
    query = "INSERT INTO salesdata(rowid, product_id, customer_id, quantity)  VALUES(?,?,?,?);"
    stmt = ibm_db.prepare(db2_conn, query)
    for row in records:
        ibm_db.execute(stmt, row)

if __name__ == '__main__':
    mysql_passwd, db2_passwd = sys.argv[1:]
    db2_conn = connect_db2(db2_passwd)

    last_row_id = get_last_rowid(db2_conn)
    print("Last row id on production datawarehouse = ", last_row_id)

    new_records = get_latest_records(last_row_id, mysql_passwd)
    print("New rows on staging datawarehouse = ", len(new_records))

    insert_records(new_records, db2_conn)
    print("New rows inserted into production datawarehouse = ", len(new_records))

    ibm_db.close(db2_conn)

