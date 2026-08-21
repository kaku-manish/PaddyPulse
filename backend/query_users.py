import sqlite3

try:
    conn = sqlite3.connect('C:/Users/kakum/Desktop/paddypulse/backend/agriculture.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT id, username, email, role FROM users")
    rows = cur.fetchall()
    
    print(f"{'ID':<5} | {'Username':<20} | {'Email':<30} | {'Role':<15}")
    print("-" * 75)
    for r in rows:
        username = r['username'] if 'username' in r.keys() else 'N/A'
        email = r['email'] if 'email' in r.keys() else 'N/A'
        role = r['role'] if 'role' in r.keys() else 'N/A'
        print(f"{str(r['id']):<5} | {str(username):<20} | {str(email):<30} | {str(role):<15}")
    
    conn.close()
except Exception as e:
    print(f"Error querying db: {e}")
