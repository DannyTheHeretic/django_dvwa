import requests
import sqlite3
import hashlib
import time
from random import randrange


passwords = [
    "123456",
    "password",
    "12345678",
    "qwerty",
    "123456789",
    "12345",
    "1234",
    "111111",
    "1234567",
    "dragon",
    "123123",
    "baseball",
    "abc123",
    "football",
    "monkey",
    "letmein",
    "696969",
    "shadow",
    "master",
    "666666",
    "qwertyuiop",
    "123321",
    "mustang",
    "1234567890",
    "michael",
    "654321",
    "pussy",
    "superman",
    "1qaz2wsx",
    "7777777",
    "fuckyou",
    "121212",
    "000000",
    "qazwsx",
    "123qwe",
    "killer",
    "trustno1",
    "jordan",
    "jennifer",
    "zxcvbnm",
    "asdfgh",
    "hunter",
    "buster",
    "soccer",
    "harley",
    "batman",
    "andrew",
    "tigger",
    "sunshine",
    "iloveyou",
    "fuckme",
    "2000",
    "charlie",
    "robert",
    "thomas",
    "hockey",
    "ranger",
    "daniel",
    "starwars",
    "klaster",
    "112233",
    "george",
    "asshole",
    "computer",
    "michelle",
    "jessica",
    "pepper",
    "1111",
    "zxcvbn",
    "555555",
    "11111111",
    "131313",
    "freedom",
    "777777",
    "pass",
    "fuck",
    "maggie",
    "159753",
    "aaaaaa",
    "ginger",
    "princess",
    "joshua",
    "cheese",
    "amanda",
    "summer",
    "love",
    "ashley",
    "6969",
    "nicole",
    "chelsea",
    "biteme",
    "matthew",
    "access",
    "yankees",
    "987654321",
    "dallas",
    "austin",
    "thunder",
    "taylor",
    "matrix"
]


def fetch_random_user():
    try:
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
    except KeyboardInterrupt:
        exit(0)
    except:
        return None

def insert_user(user):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    x = passwords[randrange(0,len(passwords))]
    t = hashlib.md5(x.encode())
    try:
        staff = 0 if randrange(0,10) < 8 else 1
        active = 0 if randrange(0,10) < 2 else 1
        c.execute("INSERT INTO auth_user (first_name, username, password, is_superuser, is_staff, is_active) VALUES (?, ?, ?, ?, ?, ?)",
                (user['first_name'], user['username'], t.hexdigest(), staff, staff, active))
        conn.commit()
    except Exception as e:
        print(e)
    conn.close()

def main():
    # Fetch a random user from the API
    random_user = fetch_random_user()
    
    if random_user:
        try:
            for i in random_user:
                insert_user(i)
            print("User inserted successfully!")
        except Exception as e:
            print(f"Failed to Update because of: {e}")
    else:
        print("Failed to fetch a random user.")

if __name__ == "__main__":
    for i in range(10000):
        main()
