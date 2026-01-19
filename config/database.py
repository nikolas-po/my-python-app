import os
from dotenv import load_dotenv

load_dotenv()

def get_database_config():
    """Получение конфигурации базы данных из переменных окружения"""
    return {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', 3306)),
        'database': os.getenv('DB_NAME', 'myapp_db'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'charset': os.getenv('DB_CHARSET', 'utf8mb4')
    }

def get_mysql_connection_string():
    """Получение строки подключения для MySQL"""
    config = get_database_config()
    return f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset={config['charset']}"
