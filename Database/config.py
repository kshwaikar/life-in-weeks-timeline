
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="dpg-d1bb6m3e5dus73eef740-a",
        database="life_in_weeks_db",
        user="ife_in_weeks_db_user",
        password=" IhIRHxd4Mz2IQb76ltvIszc4CBpbrk2u",
        port="5432"  
    )
