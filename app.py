from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME")
)

cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS visits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    count INT
)
""")

@app.route("/")
def home():
    cursor.execute("SELECT count FROM visits LIMIT 1")
    result = cursor.fetchone()

    if result:
        count = result[0] + 1
        cursor.execute("UPDATE visits SET count=%s", (count,))
    else:
        count = 1
        cursor.execute("INSERT INTO visits (count) VALUES (%s)", (count,))

    db.commit()
    return f"Hello from CI/CD Pipeline! Visit Count: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
