import pg8000.native

def get_connection():
    return pg8000.native.Connection(
        host="dpg-d1bb6m3e5dus73eef740-a",
        database="life_in_weeks_db",
        user="life_in_weeks_db_user",  
        password="IhIRHxd4Mz2IQb76ltvIszc4CBpbrk2u",
        port=5432  
    )
