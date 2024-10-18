from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# SQL Injection Vulnerability
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get('query')
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Vulnerable to SQL Injection
    cursor.execute(f"SELECT * FROM users WHERE name = '{query}'")
    results = cursor.fetchall()
    conn.close()
    
    return str(results)

# XSS Vulnerability
@app.route("/profile", methods=["GET"])
def profile():
    username = request.args.get('username')
    
    # Rendering input directly to template (Vulnerable to XSS)
    return render_template('user_profile.html', username=username)

if __name__ == "__main__":
    app.run(debug=True)
