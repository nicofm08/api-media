"""Redis client for handling redis operations."""
import redis
from app.core.logger_custom import log
from app.core.constants import LOG_CORE, REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD, REDIS_DEFAULT_EXPIRATION_TIME

class RedisClient:
    """RedisClient class to interact"""
    def __init__(self):
        self.redis = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            password=REDIS_PASSWORD,
        )
    
    async def read(self, key):
        """Read a key from redis."""
        log.info(f"{LOG_CORE} read {key}")
        return self.redis.get(key)

    async def write(self, key, value, expiration_time=REDIS_DEFAULT_EXPIRATION_TIME):
        """Write a key to redis."""
        log.info(f"{LOG_CORE} write {key} {value}")
        return self.redis.set(key, value, ex=expiration_time)

    async def publish(self, channel, message):
        """Publish a message to a channel."""
        log.info(f"{LOG_CORE} publish {channel} {message}")
        return self.redis.publish(channel, message)