import os

from dotenv import load_dotenv

# update .env
load_dotenv()

# Generate data
PHOTOS_DIR = 'app/data/photos'
PHOTO_TEMPLATE = 'app/data/template.jpg'
NEED_PHOTO = 100

# Connestion with Redis info
REDIS_HOST = os.getenv('REDIS_HOST', default='localhost')
REDIS_PORT = os.getenv('REDIS_PORT', default=6379)
REDIS_QUEUE = os.getenv('REDIS_QUEUE', default='severstal')

# Connection to DB
DB_CONNECT_DATA = {
    'database': os.getenv('POSTGRES_DB', default='postgres'),
    'user': os.getenv('POSTGRES_USER', default='postgres'),
    'password': os.getenv('POSTGRES_PASSWORD', default='postgres'),
    'host': os.getenv('POSTGRES_HOST', default='localhost'),
    'port': os.getenv('POSTGRES_PORT', default=5432),
}
