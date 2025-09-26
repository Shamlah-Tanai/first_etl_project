import psycopg
import pandas as pd
def database_connection():
    with psycopg.connect(
            host="localhost",
            dbname= "first_etl_project",
            user="postgres",
            password= "Naseer@12345",
            port=5432) as conn:
        with conn.cursor() as cur:
            sql = """
            CREATE TABLE IF NOT EXISTS students (
            id integer,
            first_name varchar,
            last_name character varying,
            date_of_birth date,
            number character(6),
            badge character(10), 
            issuing date, 
            expiration date,
            relatives integer);
            """
            cur.execute(sql)
            sql = """
            INSERT INTO students(id, first_name, last_name, date_of_birth, number, badge, issuing, expiration, relatives) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
            """
            df= pd.read_csv("../data/processed/students_cleaned.csv")
            for index, row in df.iterrows():
                cur.execute(sql, row.to_list())
                print("Sto inserendo il record di indice", index)
if __name__ == "__main__":
    database_connection()
