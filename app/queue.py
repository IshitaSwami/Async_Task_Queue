# app/queue.py
import os
from dotenv import load_dotenv
import redis
from rq import Queue

load_dotenv()

redis_conn = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    db=int(os.getenv("REDIS_DB"))
)

task_queue = Queue(connection=redis_conn)