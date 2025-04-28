import mysql.connector
mydb = mysql.connector.connect(
  host = "sql12.freesqldatabase.com",
  port = 3306,
  user = "sql12775336",
  password = "HprDPIFI9z",
  database="sql12775336"
  # ssl_ca = "/etc/ssl/certs/ca-certificates.crt",
  # ssl_verify_cert = True,
  # ssl_verify_identity = True
)
db=mydb.cursor()
# # db.execute("create table records(record_no int not null,record_name char not null,record_date date not null,Total_Entries int not null,Emp_Id int not null)")
# mydb.commit()
# # db.execute("create table test(number int)")
import random
import time
from datetime import datetime

query='insert into records (record_no,record_name,record_date,Total_Entries,Emp_Id) values (%s,%s,%s,%s,%s)'

# for i in range(1,10200):
#   data = (i,str(time.time()),str(datetime.now().date()),random.randint(1,999999),101)
#   db.execute(query,data)
# mydb.commit()
query='select * from records limit %s offset %s'
db.execute(query,(10,20))
l=db.fetchall()
print(len(l))
for record in l:
  print(record)