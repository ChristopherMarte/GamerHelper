import psycopg2

def main():
    
    conn = psycopg2.connect("dbname=gamerhelper user=test password=password")
    cur = conn.cursor()
    cur.execute("SELECT * from users")
    records = cur.fetchall()
    
    print(records)
    
main()