import redis

redis_connection = redis.Redis(host="localhost", port=6379)

print("Redis connect")

def set_value(key, value):
    redis_connection.set(key, str(value))


def get_value(key):
    redis_connection.get(key)
