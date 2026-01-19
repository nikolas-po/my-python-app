import sys
import os

# Добавляем родительскую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from config.database import get_database_config
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_database_connection():
    """Тестирование подключения к базе данных"""
    try:
        config = get_database_config()
        
        connection = mysql.connector.connect(
            host=config['host'],
            port=config['port'],
            database=config['database'],
            user=config['user'],
            password=config['password'],
            charset=config['charset']
        )
        
        if connection.is_connected():
            logger.info("✅ Успешное подключение к базе данных!")
            
            cursor = connection.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            logger.info(f"Версия MySQL: {version[0]}")
            
            cursor.close()
            connection.close()
            logger.info("Соединение закрыто.")
            
            return True
        else:
            logger.error("❌ Не удалось подключиться к базе данных")
            return False
            
    except mysql.connector.Error as err:
        logger.error(f"❌ Ошибка подключения к базе данных: {err}")
        return False
    except Exception as e:
        logger.error(f"❌ Неизвестная ошибка: {e}")
        return False

def main():
    """Основная функция приложения"""
    print("=" * 50)
    print("Python-приложение с MySQL на Debian")
    print("=" * 50)
    
    # Проверка файла .env
    if not os.path.exists('.env'):
        print("⚠️  Файл .env не найден!")
        print("Создайте его из .env.example: cp .env.example .env")
        print("Заполните своими данными")
        return
    
    if test_database_connection():
        print("✅ Подключение к базе данных успешно установлено!")
    else:
        print("❌ Ошибка подключения к базе данных")

if __name__ == "__main__":
    main()
