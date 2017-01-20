import psycopg2

def connect():
    conn = psycopg2.connect(database="organisation_structure", user='priyanshi', password='priyanshi', host="127.0.0.1")
    return conn
