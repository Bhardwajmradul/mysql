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
db = mydb.cursor()