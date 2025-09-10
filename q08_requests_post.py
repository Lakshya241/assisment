# src/q08_requests_post.py
import requests
import json

def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "OOPs Assignment", "body": "Learning Python requests", "userId": 101}
    resp = requests.post(url, json=payload, timeout=5)
    print("Status code:", resp.status_code)
    try:
        print("Response JSON:", resp.json())
    except ValueError:
        print("No JSON in response")

if __name__ == "__main__":
    main()
