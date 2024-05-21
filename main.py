import psycopg2

def main():
    
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    cur.execute("SELECT * from my_data")
    records = cur.fetchall()
    
    
    print("Start of the Journey!")
    
main()