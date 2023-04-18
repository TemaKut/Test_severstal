import os

from redis import Redis

import settings as sett
from database import DB


class PhotoThroughRedis():
    """ The class contains of two main methods: PUSH and GET to/from Redis """

    def __init__(self, redis: Redis):
        """ Initialization of class object. """
        self.redis = redis

    def bytes_of_photos_to_redis(self, photos_dir: str):
        """ Insert at start of redis queue foto bytes. """
        assert os.path.isdir(photos_dir), 'Is not a dir. or dir not exists.'

        for filename in os.listdir(photos_dir):
            full_name = f'{photos_dir}/{filename}'

            if not os.path.isfile(full_name):
                continue

            with open(full_name, 'rb') as file:
                file_bytes = file.read()

                self.redis.lpush(sett.REDIS_QUEUE, file_bytes)

    def put_data_to_database(self):
        """ The method uses the incapsulated method to put data in database """
        # DB methods object
        db = DB()

        # Iter for all objects in reddis (non-blocked)
        for bytes in self.__get_items_from_reddis_queue():
            img_weight = len(bytes)
            db.insert_values_in_table(img_weight)

    def __get_items_from_reddis_queue(self):
        """ Genetor. Get last item from redis and yield it. """
        while True:
            bytes = self.redis.rpop(sett.REDIS_QUEUE)

            if not bytes:
                continue

            yield bytes
