import psycopg2


try:
    conn = psycopg2.connect("dbname=myduka user=postgres password=444god")

    cur = conn.cursor()
except Exception as e:
    print(e)
   
def fetch_data(tbname):
    try:
        q = "SELECT * FROM " + tbname + ";"
        cur.execute(q)
        records = cur.fetchall()
        return records
    except Exception as e:
        return e
    
def insert_products(v):
    vs = str(v)
    q = "insert into products(name,buying_price,selling_price,stock_quantity) "\
        "values" + vs
    cur.execute(q)
    conn.commit()
    return q