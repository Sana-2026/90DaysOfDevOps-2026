from flask import Flask
import socket
import redis
import psycopg2

app = Flask(__name__)

hostname = socket.gethostname()

# Redis connection
redis_client = redis.Redis(host="redis", port=6379)

# Postgres connection
try:
    db = psycopg2.connect(
        host="db",
        database="mydb",
        user="postgres",
        password="postgres"
    )
    db_status = "Connected"
except Exception as e:
    db_status = f"Failed: {e}"

@app.route("/")
def home():
    try:
        redis_client.incr("hits")
        hits = redis_client.get("hits").decode("utf-8")
        redis_status = "Connected"
    except:
        hits = "0"
        redis_status = "Failed"

    return f"""
    <h1>🚀 Docker 3-Tier Demo</h1>

    <h3>Application Container</h3>
    Hostname: {hostname}

    <h3>Database Status</h3>
    Postgres: {db_status}

    <h3>Cache Status</h3>
    Redis: {redis_status}

    <h3>Page Visits (Redis Counter)</h3>
    {hits}

    <p>Refresh the page to see Redis counter increase.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
