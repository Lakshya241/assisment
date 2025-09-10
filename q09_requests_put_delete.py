# src/q09_requests_put_delete.py
import requests
import json

def do_put():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    resp = requests.put(url, json=payload, timeout=5)
    # return status and print json
    try:
        print("PUT response JSON:", resp.json())
    except ValueError:
        print("PUT response: no JSON")
    return resp.status_code

def do_delete():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    resp = requests.delete(url, timeout=5)
    return resp.status_code

if __name__ == "__main__":
    print("PUT status:", do_put())
    print("DELETE status:", do_delete())
