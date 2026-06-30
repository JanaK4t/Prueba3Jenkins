
import sqlite3

def get_user_info(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Uso de consultas parametrizadas (?) para evitar SQL Injection
    query = "SELECT * FROM users WHERE username = ?"
    
    cursor.execute(query, (username,)) 
    
    result = cursor.fetchall()
    conn.close()
    return result

username = input("Enter username: ")
user_info = get_user_info(username)
print(user_info)
