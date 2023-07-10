import psycopg2


DB_HOST="127.0.0.1"
DB_NAME="FinalProj"
DB_USER="postgres"
DB_PASS="root"


conn=psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)



cur=conn.cursor()

cur.execute("SELECT * FROM Country;")

print(cur.fetchall())

cur.close()



















conn.close()