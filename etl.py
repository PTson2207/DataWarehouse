import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

def load_staging_tabels(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    parser = configparser.ConfigParser()
    parser.read("datawarehouse.conf")

    conn = psycopg2.connect("host= {} dbname={} user={} password={} port={}".format(*parser['cluster'].values()))
    cur = conn.cursor()

    load_staging_tabels(cur, conn)
    insert_tables(conn, cur)

    conn.close()

if __name__ == "__main__":
    main()