import psycopg2

def main():
    
    conn = psycopg2.connect("dbname=gamerhelper user=test")
    cur = conn.cursor()
    cur.execute("SELECT * from games")
    records = cur.fetchall()
    
    print(records)
    
main()