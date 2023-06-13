import mysql.connector
import ibm_db

def get_data_mysql(passwd, query):
    connection = mysql.connector.connect(
        user='root',
        password=passwd,
        host='127.0.0.1',
        database='sales')

    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    connection.close()
    return records


def connect_db2(passwd):
    dsn_hostname = "55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
    dsn_uid = "bbz11106"        
    dsn_pwd = passwd      
    dsn_port = "31929"                
    dsn_database = "bludb"            
    dsn_driver = "{IBM DB2 ODBC DRIVER}"         
    dsn_protocol = "TCPIP"           
    dsn_security = "SSL"             
    dsn = (
        "DRIVER={0};"
        "DATABASE={1};"
        "HOSTNAME={2};"
        "PORT={3};"
        "PROTOCOL={4};"
        "UID={5};"
        "PWD={6};"
        "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)
    return ibm_db.connect(dsn, "", "")
    

