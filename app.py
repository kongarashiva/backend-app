from flask import Flask
import mysql.connector
 
app = Flask(__name__)
 
@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host="mysql-db",
            user="root",
            password="root123",
            database="ecommerce"
        )
        return "Backend Connected to MySQL Successfully"
    except Exception as e:
        return str(e)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
