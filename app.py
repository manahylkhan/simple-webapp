from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    db = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "mysql"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "root"),
        database=os.environ.get("DB_NAME", "testdb")
    )
    return db

@app.route("/")
def home():
    db = get_db()
    cursor = db.cursor()
    
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            count INT
        )
    """)
    
    # Get current count
    cursor.execute("SELECT count FROM visits LIMIT 1")
    result = cursor.fetchone()
    
    if result:
        count = result[0] + 1
        cursor.execute("UPDATE visits SET count=%s WHERE id=1", (count,))
    else:
        count = 1
        cursor.execute("INSERT INTO visits (count) VALUES (%s)", (count,))
    
    db.commit()
    cursor.close()
    db.close()
    
    return f"<h1>Hello from CI/CD Pipeline!</h1><h2>Visit Count: {count}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### **2️⃣ requirements.txt**
```
flask
mysql-connector-python
