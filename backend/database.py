
"""
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="neondb",
        user="neondb_owner",
        password="npg_8l3LpkBvAmxe",
        host="ep-bold-shape-afibmol1-pooler.c-2.us-west-2.aws.neon.tech",
        port="5432",
        sslmode="require"
    )
"""


import psycopg2

def get_connection():
    return  psycopg2.connect(
        host="db.causweuhihdqbfpgkqxi.supabase.co",
        port=5432,
        database="postgres",
        user="postgres",
        password="1453Wms1453",  # Supabase şifreni buraya yaz
        sslmode="require"          # Supabase bağlantısı için gerekli
    )
