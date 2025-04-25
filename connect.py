import mysql.connector
mydb = mysql.connector.connect(
  host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
  port = 4000,
  user = "2n8ca3An3YaETcW.root",
  password = "cvS715s6tLemjHl3",
  # ssl_ca = "/etc/ssl/certs/ca-certificates.crt",
  # ssl_verify_cert = True,
  # ssl_verify_identity = True
)
# mydb.cursor().execute("create database if not exists school")
mydb.cursor().execute("use school")
db = mydb.cursor()
# db.execute("Truncate table records")
# mydb.commit()
query="insert into records (record_no,record_name,record_date,no_of_entries,Emp_Id) values (%s,%s,%s,%s,%s)"
import random
import time
from datetime import datetime

db.execute('insert into records (record_no,record_name,record_date,no_of_entries,Emp_Id) values (1,"hello","2025-01-01",111,101)')
mydb.commit()
# for i in range(1,2):
#   # data = (i,str(time.time()),str(datetime.now().date()),random.randint(1,999999),101)
#   db.execute(query,data)
# mydb.commit()