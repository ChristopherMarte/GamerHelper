import psycopg2

def main():
    
    conn = psycopg2.connect("dbname=test user=test")
    cur = conn.cursor()
    cur.execute("SELECT * from data")
    records = cur.fetchall()
    
    print("Start of the Journey!")
    
main()