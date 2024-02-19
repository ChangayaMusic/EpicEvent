# views.py
import json
import jwt
import getpass
from datetime import datetime, timedelta
import mysql.connector
from .models import JwtToken

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Y@mahatdr1125',
    'database': 'epic_event_auth',
    'port': 3306,
}

API_BASE_URL = "http://votre_domaine.com/api/"  # Replace with your API base URL

def login(username, password):
    url = f"{API_BASE_URL}login/"
    data = {'username': username, 'password': password}

    # Assume you have a `post` function to send HTTP POST requests
    response = post(url, json=data)
    if response.status_code == 200:
        token = response.json().get('token')
        save_token(username, token)
        print("Authentication successful. Token has been saved.")
    else:
        print(f"Authentication failed. Error message: {response.json().get('error')}")

def save_token(username, token):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    # Insert or update the token in the database
    cursor.execute("INSERT INTO jwt_token (username, token) VALUES (%s, %s) ON DUPLICATE KEY UPDATE token = VALUES(token)", (username, token))
    connection.commit()

    cursor.close()
    connection.close()

def load_token(username):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)

    # Retrieve the token from the database
    cursor.execute("SELECT token FROM jwt_token WHERE username = %s", (username,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result.get('token') if result else None

def protected_resource(username):
    token = load_token(username)

    if token:
        protected_resource_url = f"{API_BASE_URL}protected/"
        headers = {'Authorization': f'Bearer {token}'}

        # Assume you have a `get` function to send HTTP GET requests
        response = get(protected_resource_url, headers=headers)

        if response.status_code == 200:
            print(f"Response from protected resource: {response.json()}")
        else:
            print(f"Failed to access protected resource. Error message: {response.json()}")
    else:
        print("No valid token found. Please log in first.")
