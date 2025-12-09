import pandas as pd
from sqlalchemy import create_engine
import psycopg2

# Данные для подключения
DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'database': 'your_database',
    'user': 'your_username',
    'password': 'your_password'
}

def load_data_to_postgres():
    """Базовый пример загрузки данных в PostgreSQL"""
    
    # 1. Создаем подключение через SQLAlchemy (рекомендуется)
    connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    engine = create_engine(connection_string)
    
    # 2. Создаем тестовый DataFrame
    data = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Иван', 'Мария', 'Алексей', 'Ольга', 'Дмитрий'],
        'age': [25, 30, 35, 28, 40],
        'salary': [50000, 60000, 75000, 55000, 80000],
        'department': ['IT', 'Маркетинг', 'IT', 'Финансы', 'Маркетинг']
    }
    df = pd.DataFrame(data)
    
    # 3. Загружаем данные в таблицу
    table_name = 'employees'
    
    # Если таблица существует - заменяем, если нет - создаем
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',  # 'replace', 'append', 'fail'
        index=False
    )
    
    print(f"Данные успешно загружены в таблицу '{table_name}'")
    print(f"Количество строк: {len(df)}")
    
    # Закрываем подключение
    engine.dispose()

if __name__ == "__main__":
    load_data_to_postgres()


    