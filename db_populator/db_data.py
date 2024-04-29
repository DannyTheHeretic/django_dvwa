import requests
import sqlite3
import hashlib
import time

def fetch_random_user():
    url = "https://random-data-api.com/api/users/random_user?size=100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        time.sleep(1)
        url = "https://random-data-api.com/api/users/random_user?size=100"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        print("Failed to fetch data from API")
        return None

def insert_user(user):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    x = user['password']
    t = hashlib.md5(x.encode())
    print(t.hexdigest())
    try:
        c.execute("INSERT INTO auth_user (id, first_name, last_name, username, password, email, is_superuser, is_staff, is_active, date_joined) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (user['id'], user['first_name'], user['last_name'], user['username'], t.hexdigest(), user['email'], False, False, True, 0))
        conn.commit()
    except:
        pass
    conn.close()

def main():
    # Fetch a random user from the API
    random_user = fetch_random_user()
    
    if random_user:
        # Insert the user into the database
        try:
            for i in random_user:
                insert_user(i)
            print("User inserted successfully!")
        except Exception as e:
            print(f"Failed to Update because of: {e}")
    else:
        print("Failed to fetch a random user.")

if __name__ == "__main__":
    main()
