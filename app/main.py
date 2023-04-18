from threading import Thread

from redis import Redis

from data.utils import fill_dir_with_photos
import settings as sett
from utils import PhotoThroughRedis


if __name__ == '__main__':
    # Fill some dir with photos if photos does not exists
    fill_dir_with_photos(sett.PHOTOS_DIR, sett.PHOTO_TEMPLATE, sett.NEED_PHOTO)

    # Put to redis and get bytes from redis in different Threads
    with Redis(host=sett.REDIS_HOST, port=sett.REDIS_PORT) as redis:
        # Creating n photos
        photo_through_redis = PhotoThroughRedis(redis)

        # Start tasks Threads
        t1 = Thread(
            target=photo_through_redis.bytes_of_photos_to_redis,
            args=(sett.PHOTOS_DIR,),
        )

        t2 = Thread(
            target=photo_through_redis.put_data_to_database,
            args=(),
        )

        t1.start()
        t2.start()

        t1.join()
        t2.join()
